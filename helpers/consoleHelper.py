"""
Modified from https://zxq.co/ripple/pep.py/src/branch/master/helpers/consoleHelper.py
"""

from common.constants import bcolors
from objects import glob

def printServerStartHeader(asciiArt=True):
	"""
	Print server start message

	:param asciiArt: print BanchoBoat ascii art. Default: True
	:return:
	"""
	if asciiArt:
		print("""
 {b}▒{f}█████    ██████  █    ██  ▐██▌   █████{b}▒{f}██   ██{b}▒
▒{f}██{b}▒  {f}██{b}▒▒{f}██    {b}▒  {f}██  {b}▓{f}██{b}▒ {f}▐██▌ {b}▓{f}██   {b}▒▒▒ {f}█ █ {b}▒░
▒{f}██{b}░  {f}██{b}▒░ ▓{f}██▄   {b}▓{f}██  {b}▒{f}██{b}░ {f}▐██▌ {b}▒{f}████ {b}░░░  {f}█   {b}░
▒{f}██   ██{b}░  ▒   {f}██{b}▒▓▓{f}█  {b}░{f}██{b}░ ▓{f}██{b}▒ ░▓{f}█{b}▒  ░ ░ {f}█ █ {b}▒
░ {f}████{b}▓▒░▒{f}██████{b}▒▒▒▒{f}█████{b}▓  ▒{f}▄▄  {b}░▒{f}█{b}░   ▒{f}██{b}▒ ▒{f}██{b}▒
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ░{f}▀▀{b}▒  ▒ ░   ▒▒ ░ ░▓ ░
  ░ ▒ ▒░ ░ ░▒  ░ ░░░▒░ ░ ░  ░  ░  ░     ░░   ░▒ ░
░ ░ ░ ▒  ░  ░  ░   ░░░ ░ ░     ░  ░ ░    ░    ░
    ░ ░        ░     ░      ░            ░    ░
{e}""".format(f="\033[35m", b="\033[34m", e=bcolors.ENDC))

	printColored("> Welcome to ci-system v{}".format(glob.VERSION), bcolors.GREEN)
	printColored("> Made by Sunpy", bcolors.GREEN)
	printColored("> {}https://github.com/osufx/ci-system".format(bcolors.UNDERLINE), bcolors.GREEN)
	printColored("> Press CTRL+C to exit\n", bcolors.GREEN)

def printNoNl(string):
	"""
	Print a string without \n at the end

	:param string: string to print
	:return:
	"""
	print(string, end="")

def printColored(string, color):
	"""
	Print a colored string

	:param string: string to print
	:param color: ANSI color code
	:return:
	"""
	print("{}{}{}".format(color, string, bcolors.ENDC))

def printError():
	"""
	Print a red "Error"

	:return:
	"""
	printColored("Error", bcolors.RED)

def printDone():
	"""
	Print a green "Done"

	:return:
	"""
	printColored("Done", bcolors.GREEN)

def printWarning():
	"""
	Print a yellow "Warning"

	:return:
	"""
	printColored("Warning", bcolors.YELLOW)
