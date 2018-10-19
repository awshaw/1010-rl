import math
from gym.envs.registration import register

register(
    id='TenTen-v0',
    entry_point='gym-1010.envs:TenTenEnv',
    max_episode_steps=9999999,
    reward_threshold=9999999,
    kwargs={'max_steps': math.inf},
    nondeterministic=True
)