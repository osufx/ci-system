"""
A lot of this has been taken directly from https://zxq.co/ripple/pep.py/src/branch/master/pep.py
and modified to fit the project.

I dont see the reason to reinvent the structure if this is suppost to work alongside the original project.
"""
import redis
import sys

from helpers import consoleHelper, configHelper
from common.constants import bcolors
from objects import glob
import redis_subscriber

import time

if __name__ == "__main__":
	try:
		# Server start
		consoleHelper.printServerStartHeader(True)

		# Read config.ini
		consoleHelper.printNoNl("> Loading config file...")
		glob.conf = configHelper.config("config.ini")

		if glob.conf.default:
			# We have generated a default config.ini, quit server
			consoleHelper.printWarning()
			consoleHelper.printColored("[!] config.ini not found. A default one has been generated.", bcolors.YELLOW)
			consoleHelper.printColored("[!] Please edit your config.ini and run the server again.", bcolors.YELLOW)
			sys.exit()

		# If we haven't generated a default config.ini, check if it's valid
		if not glob.conf.checkConfig():
			consoleHelper.printError()
			consoleHelper.printColored("[!] Invalid config.ini. Please configure it properly", bcolors.RED)
			consoleHelper.printColored("[!] Delete your config.ini to generate a default one", bcolors.RED)
			sys.exit()
		else:
			consoleHelper.printDone()

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