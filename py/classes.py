#!/usr/bin/env python3

import character

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
