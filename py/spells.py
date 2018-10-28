#!/usr/bin/env python

class Spell:
    def __init__(self, name, desc, level, classes, school, cast, castRange, components, concentration, ritual):
        self.name = name
        self.desc = desc
        self.level = level
        self.classes = classes
        self.school = school
        self.cast = cast
        self.castRange = castRange
        self.components = components
        self.concentration = concentration
        self.ritual = ritual

    def get_school(self):
        return self.school
    def get_name(self):
        return self.name
    def get_desc(self):
        return self.desc
    def get_level(self):
        return self.level
    def get_cast(self):
        return self.cast
    def get_classes(self):
        return self.classes
    def get_components(self):
        return self.components
    def get_range(self):
        return self.castRange
    def is_concentration(self):
        return self.contentration
    def is_ritual(self):
        return self.ritual

    def __repr__(self):
        return 'name:%s;level:%s;classes:%s;school:%s;cast:%s;castRange:%s;components:%s;concentration:%s;ritual:%s;desc:%s;' % (self.name, self.level, self.classes, self.school, self.cast, self.castRange, self.components, self.concentration, self.ritual, self.desc)

if __name__ == "__main__":
    burningHands = Spell("Burning Hands","You shoot hot fire bro",1,"Wizard","Evocation","Action","30 ft cone","VSM",False,False)
    repre = repr(burningHands)
    print(repre)

