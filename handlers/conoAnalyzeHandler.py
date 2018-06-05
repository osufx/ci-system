from common.redis import generalPubSubHandler
from objects import glob

class handler(generalPubSubHandler.generalPubSubHandler):
    def __init__(self):
        super().__init__()
        self.structure = {
			"score_id": 0,
			"beatmap_id": 0,
            "user_id": 0,
            "replay_data": ""
		}
    
    def handle(self, data):
        data = super().parseData(data)
        if data is None:
            return
        # TODO: scan data and report back