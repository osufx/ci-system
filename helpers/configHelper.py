"""
Modified from https://zxq.co/ripple/pep.py/src/branch/master/helpers/configHelper.py
"""

import os
import configparser

class config:
	# Check if config.ini exists and load/generate it
	def __init__(self, file):
		"""
		Initialize a config file object

		:param file: file name
		"""
		self.config = configparser.ConfigParser()
		self.default = True
		self.fileName = file
		if os.path.isfile(self.fileName):
			# config.ini found, load it
			self.config.read(self.fileName)
			self.default = False
		else:
			# config.ini not found, generate a default one
			self.generateDefaultConfig()
			self.default = True


	# Check if config.ini has all needed the keys
	def checkConfig(self):
		"""
		Check is the config file has all required keys

		:return: True if valid, False if not valid
		"""
		try:
			# Try to get all the required keys
			self.config.get("redis","host")
			self.config.get("redis","port")
			self.config.get("redis","database")
			self.config.get("redis","password")

			self.config.get("debug","enable")

			self.config.get("discord","enable")
			self.config.get("discord","webhook")
			return True
		except configparser.Error:
			return False

	def generateDefaultConfig(self):
		"""
		Write a default config file to disk

		:return:
		"""
		# Open config.ini in write mode
		f = open(self.fileName, "w")

		# Set keys to config object
		self.config.add_section("redis")
		self.config.set("redis", "host", "localhost")
		self.config.set("redis", "port", "6379")
		self.config.set("redis", "database", "0")
		self.config.set("redis", "password", "")

		self.config.add_section("debug")
		self.config.set("debug", "enable", "0")

		self.config.add_section("discord")
		self.config.set("discord", "enable", "0")
		self.config.set("discord", "webhook", "")

		# Write ini to file and close
		self.config.write(f)
		f.close()
