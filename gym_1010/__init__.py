from gym.envs.registration import register

register(
    id='1010-v0',
    entry_point='gym_1010.envs:TenTenEnv',
    timestep_limit=1000,
)