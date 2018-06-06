import threading

from common.redis import generalPubSubHandler
from objects import glob
from tasks import replay_analyze

class handler(generalPubSubHandler.generalPubSubHandler):
	def __init__(self):
		super().__init__()
		self.structure = {
			"score_id": 0,
			"beatmap_id": 0,
			"user_id": 0,
			"game_mode": 0,
			"pp": 0,
			"replay_data": ""
		}
	
	def handle(self, data: bytes):
		data = super().parseData(data)
		if data is None:
			return

		threading.Thread(
			replay_analyze.Analyze(data)
		).start()