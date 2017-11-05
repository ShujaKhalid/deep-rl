# Import the openAI gym module
import gym

# Create an environment for the specific game - "breakout"
env = gym.make('BreakoutDeterministic-v4')

# Reset the frame to start from the first frame
frame = env.reset()

# Render
env.render()

is_done = False
while not is_done:
	# Perform an action that is random by sampling the action space
	# Note: No feedback is used here. The reward function is ignored.
	frame, reward, is_done, _ = env.step(env.action_space.sample())

	# debugging
	print('reward=' + str(reward)) # debug

	# Render the frame with the given action
	env.render()

