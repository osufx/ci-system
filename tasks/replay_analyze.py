import os
import base64

from objects.replay import Replay
from objects.beatmap_parser.osu_parser.beatmap import Beatmap
from objects import glob

class Analyze(object):
	score_id	= 0
	beatmap_id	= 0
	user_id		= 0
	game_mode	= 0
	pp			= 0
	replay 		= None
	beatmap		= None
	
	def __init__(self, data: dict):
		# Put data types into self
		for key, value in data.items():
			if key is not "replay_data":
				setattr(self, key, value)

		self.ParseReplay(data["replay_data"])

		# Check if replay is not matching the rest of the data
		self.CheckMissmatchReplay()

		beatmap_path = glob.conf.config["paths"]["lets"] + "/.data/beatmaps/{}.osu".format(self.beatmap_id)

		# Check if file exists
		if not os.path.isfile(beatmap_path):
			print("Missing beatmap_id {} for score_id {}".format(self.beatmap_id, self.score_id))
			raise Exception("Missing beatmap")

		self.beatmap = Beatmap(beatmap_path)

		#TODO: Do the analyze stuffz
	
	def ParseReplay(self, base64_replay_data: str):
		replay_bytes = base64.b64decode(base64_replay_data)
		self.replay = Replay(replay_bytes)
	
	def CheckMissmatchReplay(self):
		#beatmap_id
		#TODO: Get beatmap more info and do check

	def getAverageTickRate(self):
		pass