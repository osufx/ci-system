try:
	with open("version") as f:
		VERSION = f.read().strip()
	if VERSION == "":
		raise Exception
except:
	VERSION = "Unknown"

conf = None
redis = None
