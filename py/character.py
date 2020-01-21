#!/usr/bin/env python3

class CharacterSheetClass:
	def __init__(self):
		self.scores = {"STR": 0,
			"DEX": 0,
			"CON": 0,
			"WIS": 0,
			"INT": 0,
			"CHA": 0
		}
		self.name = ""
		self.race = ""
		self.classes = []
		self.level = 0
	def set_name(self,name):
		self.name = name
	def get_name(self):
		return self.name
	def level_up(self,a_class):
		found = 0 
		for i_class in self.classes:
			if(i_class.name == a_class):
				i_class.level_up()
				found = 1 
				break
		if not found:
			self.classes.append(self._new_class(a_class))
		self.level = self.level+1
		print("level up!")
	def _new_class(self,a_class):
		if a_class == "barbarian":
			return BarbarianClassClass(1)
		elif a_class == "fighter":
			return FighterClassClass(1)


