import pygame
import pieces
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


WIDTH = 30
HEIGHT = 30
MARGIN = 3

grid = np.zeros((10,10)).astype(int)
p_space = np.zeros((10,10)).astype(int)

def main():
    pygame.init()
    WINDOW_SIZE = [333, 460]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("1010!")
    done = False
    clock = pygame.time.Clock()

    hand = pieces.rand_hand()
    # print(hand)

    _selected = None
    _pieces = [0, 1, 2]

    score = 0
    count = 0

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            #TODO: Clean up logic and make object oriented for clarity
            elif event.type == pygame.KEYDOWN:

                locs = np.where(p_space == 2)

                if len(locs[1]) > 0:

                    if event.key == pygame.K_a:
                        if 1 <= min(locs[1]) <= 9:
                            p_space[locs[0], locs[1]] = 0
                            p_space[locs[0], locs[1] - 1] = 2
                            locs = np.where(p_space == 2)

                    elif event.key == pygame.K_d:
                        if 0 <= max(locs[1]) < 9:
                            p_space[locs[0], locs[1]] = 0
                            p_space[locs[0], locs[1] + 1] = 2
                            locs = np.where(p_space == 2)

                    elif event.key == pygame.K_w:
                        if 1 <= min(locs[0]) <= 9:
                            p_space[locs[0], locs[1]] = 0
                            p_space[locs[0]-1, locs[1]] = 2
                            locs = np.where(p_space == 2)

                    elif event.key == pygame.K_s:
                        if 0 <= max(locs[0]) < 9:
                            p_space[locs[0], locs[1]] = 0
                            p_space[locs[0]+1, locs[1]] = 2
                            locs = np.where(p_space == 2)

                    # Return piece to hand, do not place
                    elif event.key == pygame.K_q:
                        p_space[locs[0], locs[1]] = 0
                        _selected = None

                    # Place piece
                    elif event.key == pygame.K_e:
                        elem_sum = np.sum([p_space[locs[0], locs[1]], grid[locs[0], locs[1]]], axis=0)
                        # print(elem_sum)
                        illegal_count = np.where(elem_sum >= 3)
                        # print(np.shape(illegal_count)[1])

                        if np.shape(illegal_count)[1] == 0:
                            p_space[locs[0], locs[1]] = 0
                            grid[locs[0], locs[1]] = 2

                            _pieces.remove(_selected)

                            # Update score for placed piece
                            score += (np.sum(elem_sum)/2)

                elif event.key == pygame.K_1:
                    # print(_pieces)
                    if 0 in _pieces:
                        p = 2*hand[0].astype(int)
                        # print(p)
                        px = p.shape[0]
                        py = p.shape[1]

                        p_space[5:5+px, 5:5+py] += p

                        _selected = 0

                    else:
                        break

                elif event.key == pygame.K_2:
                    # print(_pieces)
                    if 1 in _pieces:
                        p = 2*hand[1].astype(int)
                        # print(p)
                        px = p.shape[0]
                        py = p.shape[1]

                        p_space[5:5+px, 5:5+py] += p

                        _selected = 1

                    else:
                        break
                elif event.key == pygame.K_3:
                    # print(_pieces)
                    if 2 in _pieces:
                        p = 2 * hand[2].astype(int)
                        # print(p)
                        px = p.shape[0]
                        py = p.shape[1]

                        p_space[5:5 + px, 5:5 + py] += p

                        _selected = 2

                        # pieces.does_it_fit()
                    else:
                        break

        # Clear rows and columns
        rows_to_clear = np.where(grid.sum(axis=1) >= 20)
        columns_to_clear = np.where(grid.sum(axis=0) >= 20)

        score += (len(rows_to_clear[0]) + len(columns_to_clear[0])) * 10
        for l in rows_to_clear[0]:
            grid[l, ] = 0
        for l in columns_to_clear[0]:
            grid[:, l] = 0

        # print(_pieces)
        # print(count)

        # Check if game can continue
        if len(_pieces) > 0:
            for i in _pieces:
                p = hand[i]
                #print(p)
                count = 0
                # print(np.sum(p))
                x = p.shape[0]
                y = p.shape[1]
                for i in range(10):
                    if i + x <= 10:
                        for j in range(10):
                            if j + y <= 10:
                                ew_sum = np.sum([2*p, grid[i:i + x, j:j + y]])
                                if ew_sum <= 2*np.sum(p):
                                    count += 1
        else:
            hand = pieces.rand_hand()
            _pieces = [0, 1, 2]
            count = 999999

        if count == 0:
            print(grid)
            for i in _pieces:
                print(hand[i])
            done = True


        screen.fill(BLACK)

        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                if grid[row][column] >= 2:
                    color = GREEN
                if p_space[row][column] == 2:
                    color = BLUE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Draw pieces
        for p in _pieces:
            tmp = hand[p]
            for i in range(tmp.shape[0]):
                for j in range(tmp.shape[1]):
                    color = BLACK
                    if tmp[i, j] == 1:
                        color = GREEN
                    pygame.draw.rect(screen,
                                     color,
                                     [p*100 + (MARGIN + 15) * (j+1) + MARGIN,
                                      350 + (MARGIN + 15) * (i+1) + MARGIN,
                                      15, 15])

        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score {}".format(score), True, RED)
        screen.blit(text, [200, 420])

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
