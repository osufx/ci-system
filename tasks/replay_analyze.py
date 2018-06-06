import base64
from objects.replay import Replay

class Analyze(object):
	score_id	= 0
	beatmap_id	= 0
	user_id		= 0
	game_mode	= 0
	pp			= 0
	replay 		= None
	
	def __init__(self, data: dict):
		# Put data types into self
		for key, value in data.items():
			if key is not "replay_data":
				setattr(self, key, value)

		self.ParseReplay(data["replay_data"])

		#TODO: Do the analyze stuffz
	
	def ParseReplay(self, base64_replay_data: str):
		replay_bytes = base64.b64decode(base64_replay_data)
		self.replay = Replay(replay_bytes)
		