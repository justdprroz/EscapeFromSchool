import json

class plotDriver:
	def loadPlotFromJSON(self):
		with open("plot.json", "r") as plotFile:
			self.plotData = json.load(plotFile)
	def __init__(self):
		self.plotData = None
		self.currentNode = None
		loadPlotFromJSON()

	def doTurn(index):
		variants = list(self.currentNode.keys())
		if (index < 0 or index > len(variants)):
			return 0
		self.currentNode = self.currentNode[variants[index]]
		if isinstance(self.currentNode, str):
			return 2
		if isinstance(self.currentNode, dict):
			return 1

	def getVariant():
		return self.currentNode

if "__name__" == "__main__":
	print("hello")