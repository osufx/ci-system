import redis
from common.redis import pubSub
from objects import glob

from handlers import conoAnalyzeHandler

def subscribe():
    # Connect to pubsub channels
    pubSub.listener(glob.redis, {
        "cono:analyze": conoAnalyzeHandler.handler()
    }).start()