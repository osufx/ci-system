"""
A lot of this has been taken directly from https://zxq.co/ripple/pep.py/src/branch/master/pep.py
and modified to fit the project.

I dont see the reason to reinvent the structure if this is suppost to work alongside the original project.
"""
import redis

from helpers import consoleHelper
from common.constants import bcolors
from objects import glob
import redis_subscriber

import time

if __name__ == "__main__":
	try:
		# Server start
		consoleHelper.printServerStartHeader(True)

		# Config-setup be here
		#----

		# Connect to redis
		try:
			consoleHelper.printNoNl("> Connecting to redis... ")
			#glob.redisglob.redis = redis.Redis(glob.conf.config["redis"]["host"], glob.conf.config["redis"]["port"], glob.conf.config["redis"]["database"], glob.conf.config["redis"]["password"])
			glob.redis = redis.Redis("localhost", "6379", "0", "")
			glob.redis.ping()
			consoleHelper.printNoNl(" ")
			consoleHelper.printDone()
		except:
			# Exception while connecting to db
			consoleHelper.printError()
			consoleHelper.printColored("[!] Error while connection to redis. Please check your config.ini and run the server again", bcolors.RED)
			raise

		# Subscribe to redis events 
		consoleHelper.printColored("> Subscribing to redis events... ", bcolors.YELLOW)
		redis_subscriber.subscribe()
		consoleHelper.printDone()

		while True: # Makeshift (PLEASE CHANGE)
			time.sleep(1)
	finally:
		print("> Disposing server... ")
		# glob.fileBuffers.flushAll() #Maybe I will need something like this? I am not using any files on disk atm.
		consoleHelper.printColored("Goodbye!", bcolors.GREEN)