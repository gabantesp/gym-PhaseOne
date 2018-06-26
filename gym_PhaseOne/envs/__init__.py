from gym_PhaseOne.envs.PhaseOne_env import PhaseOneEnv
from gym_PhaseOne.envs.PhaseOne_extrahard_env import PhaseOneExtraHardEnv
from gym.envs.registration import register 

register(
  id = 'PhaseOne-v0',
  entry_point = 'PhaseOne.PhaseOne:PhaseOne',
)
