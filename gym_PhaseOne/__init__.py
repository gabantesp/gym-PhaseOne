from gym.envs.registration import register

register(
    id='PhaseOne-v0',
    entry_point='gym_PhaseOne.envs:PhaseOneEnv',
)
register(
    id='PhaseOne-extrahard-v0',
    entry_point='gym_PhaseOne.envs:PhaseOneExtraHardEnv',
)
