#!/usr/bin/env python

class CharacterSheetClass:
    def __init__(self,name,race,classClass,level):
        self.name = name
        self.race = race
        self.classClass = classClass
        self.level = level


    #Class classes

class BaseClassClass:
    levelMap = {'1': 'Level 1', '2': 'Level 2', '3' : 'Level 3', '4': 'ASI', '5': 'Level 5'}

class BarbarianClassClass(BaseClassClass):
    def __init__(self,level):
        self.hitDie = 12
        self.armorProf = ["Light Armor", "Medium Armor", "Shields"]
        self.weaponProf = ["Simple Weapons", "Martial Weapons"]
        self.toolProf = []


class BardClassClass(BaseClassClass):
	pass
class ClericClassClass(BaseClassClass):
	pass
class DruidClassClass(BaseClassClass):
	pass
class FighterClassClass(BaseClassClass):
	pass
class MonkClassClass(BaseClassClass):
	pass
class PaladinClassClass(BaseClassClass):
	pass
class RogueClassClass(BaseClassClass):
	pass
class RangerClassClass(BaseClassClass):
	pass
class SorcererClassClass(BaseClassClass):
	pass
class WarlockClassClass(BaseClassClass):
	pass
class WizardClassClass(BaseClassClass):
	pass

    #Modifiers classes

class BaseMod:
    def __init__(self, value, mod_type):
        self.value = value
        self.mod_type = mod_type

class StaticMod(BaseMod):
    def __init__(self, value, mod_type):
        self.value = value
        self.mod_type = mod_type

class DynamicMod(BaseMod):
    def __init__(self, value, mod_type):
        self.value = value
        self.mod_type = mod_type

class SituationalMod(BaseMod):
    def __init__(self, value, mod_type):
        self.value = value
        self.mod_type = mod_type

    #Action classes

class ActionClass:
    def __init__(self, desc, name)
        self.name = name
        self.desc = desc

class FullAction(ActionClass):

class BonusAction(ActionClass):

class MoveAction(ActionClass):  #Modifier describes amount of character movement - .5 is half movement (standing from prone), etc.
    def __init__(self, desc, name, modifier):
        self.name = name
        self.desc = desc
        self.mod = modifier

class ReactionAction(ActionClass):

class FreeAction(ActionClass):
