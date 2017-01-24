from gym.envs.registration import registry, register, make, spec

# Space Fortress
# ----------------------------------------
for game in ['AIM', 'SF', 'SFS', 'SFC']:
	register(
		id='{}-v0'.format(game),
		entry_point='gym.envs.space_fortress:SFEnv',
		kwargs={'game': game,}
	)
