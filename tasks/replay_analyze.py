import base64
from objects.replay import Replay

class Analyze(object):
	def __init__(self, data):
		self.data = data
		self.ParseReplay()

		#TODO: Do the analyze stuffz
	
	def ParseReplay(self):
		replay_bytes = base64.b64decode(self.data["replay_data"])
		del(self.data["replay_data"])

		self.replay = Replay(replay_bytes)