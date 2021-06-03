import json

class plotDriver:
	def loadPlotFromJSON(self):
		with open("plot.json", "r") as plotFile:
			self.plot = json.load(plotFile)
			
	def __init__(self):
		self.plot = None
		self.loadPlotFromJSON()
		self.isEnded = False

	def doTurn(self, index):
		if self.isEnded:
			return 0
		variants = list(self.plot.keys())
		if (index < 0 or index > len(variants)):
			return 0
		self.currentNode = self.plot[variants[index]]
		if isinstance(self.plot, str):
			self.isEnded = True
			return 1
		if isinstance(self.plot, dict):
			return 1

	def getVariant(self):
		if not self.isEnded:
			variants = list(self.plot.keys())
		if self.isEnded:
			variants = self.plot
		return variants