import json

class plotDriver:
	def loadPlotFromJSON(self):
		with open("../plot.json", "r") as plotFile:
			self.plot = json.load(plotFile)

	def __init__(self):
		self.plot = None
		self.loadPlotFromJSON()
		self.isEnded = False

	def doTurn(self, index):
		variants = list(self.plot[1].keys())
		if (index < 0 or index > (len(variants) - 1)):
			return 0
		self.plot = self.plot[1][variants[index]]
		if self.plot == dict():
			self.isEnded = True
		return 1

	def getText(self):
		text = plot[0]
		return text

	def getVariants(self):
		variants = list(self.plot.keys())
		return variants