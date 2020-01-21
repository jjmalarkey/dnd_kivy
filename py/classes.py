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


    #Class classes

class BaseClassClass:
	def __init__(self):
		self.levelMap = {1: '', 
		2: '', 
		3: '', 
		4: 'ASI', 
		5: '', 
		6: ''
		}
		self.level = 1
	def level_up(self):
		self.level = self.level+1
		if(self.levelMap[self.level] != ''):
			print("got this: " + self.levelMap[self.level])

class MultiClass:
	def __init__(self, armorProf, weaponProf, toolProf, skillProf):
		if(len(armorProf)):
			self.armorProf = armorProf
		if(len(weaponProf)):
			self.weaponProf = weaponProf
		if(len(toolProf)):
			self.toolProf = toolProf
		if(len(skillProf)):
			self.skillProf = skillProf
	
#actual classes

class BarbarianClassClass(BaseClassClass, MultiClass):
	def __init__(self,level):
		self.name = "barbarian"
		super().__init__()
		self.hitDie = 12
		self.armorProf = ["Light Armor", "Medium Armor", "Shields"]
		self.weaponProf = ["Simple Weapons", "Martial Weapons"]
		self.toolProf = []
		MultiClass.__init__(self, [], ["Martial Weapons", "Simple Weapons"], [], [])

class FighterClassClass(BaseClassClass):
	def __init__(self,level):
		self.name = "fighter"
		super().__init__()
		self.hitDie = 10
		self.armorProf = ["Light Armor", "Medium Armor", "Heavy Armor", "Shields"]
		self.weaponProf = ["Simple Weapons", "Martial Weapons"]
		self.toolProf = []
		self.levelMap[6] = 'ASI'

if __name__ == "__main__":
	print("woops")
