import pygame
import numpy as np

import pieces

class TenTen:


	def __init__(self):
		# Pygame configs
		pygame.init()
		pygame.display.set_caption("1010!")

		self.clock = pygame.time.Clock()
		self.done = False
		self.screen = pygame.display.set_mode([333, 460])

		# Visuals
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.font = pygame.font.SysFont('Calibri', 25, True, False)

		self.BLACK = (0, 0, 0)
		self.BLUE = (0, 0, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)
		self.WHITE = (255, 255, 255)

		self.HEIGHT = self.WIDTH = 30
		self.MARGIN = 3

        # Initial config
        self.count = 0
        self.hand = pieces.rand_hand()
        self.grid = np.zeros((10, 10))
        self.max_steps = 99999
        self.score = 0
        self.step_number = 0
        self.play_grid = np.zeros((10, 10))

        self._pieces = [0, 1, 2]
        self._selected = None

        # Initial grid
        self.update_grid()

    def 


    def place_piece(self, current_piece, play_grid, grid, score):
    	# Current location of piece
    	locs = np.where(play_grid == 2)

		elem_sum = np.sum([play_grid[locs[0], locs[1]], grid[locs[0], locs[1]]], axis=0)
		# print(elem_sum)
		illegal_count = np.where(elem_sum >= 3)
		# print(np.shape(illegal_count)[1])

		if np.shape(illegal_count)[1] == 0:
			play_grid[locs[0], locs[1]] = 0
			grid[locs[0], locs[1]] = 2

			self._pieces.remove(current_piece)

			# Update score for placed piece
			score += (np.sum(elem_sum)/2)


    def quit_game(self):
        try:
            self.__game_over = True
            pygame.display.quit()
            pygame.quit()
       	except:
       		pass


	def update(self, grid, play_grid):
        for row in range(10):
        	for column in range(10):
            	color = WHITE
	            if grid[row][column] == 1:
	                color = GREEN
	            if grid[row][column] >= 2:
	                color = GREEN
	            if play_grid[row][column] == 2:
	                color = BLUE
	            pygame.draw.rect(screen,
	                             color,
	                             [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
	                              (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
	                              self.WIDTH,
	                              self.HEIGHT])

        text = self.font.render("Score {}".format(score), True, RED)
        self.screen.blit(text, [200, 420])