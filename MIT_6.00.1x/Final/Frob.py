# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob: a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    # By Huang Geyang
    if newFrob.myName() >= atMe.myName():
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            return
        else:
            if newFrob.myName() <= atMe.getAfter().myName():
                # insert newFrob
                newFrob.setAfter(atMe.getAfter())
                newFrob.setBefore(atMe)
                atMe.getAfter().setBefore(newFrob)
                atMe.setAfter(newFrob)
            else:
                return insert(atMe.getAfter(), newFrob)
    else:
        if atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            return
        else:
            return insert(atMe.getBefore(), newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    # By Huang Geyang
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())

# testing

mark = Frob('mark')
craig = Frob('craig')
jayne = Frob('jayne')
martha = Frob('martha')
nick = Frob('nick')
sam = Frob('sam')
xanthi = Frob('xanthi')

insert(sam,nick)
insert(nick, xanthi)
insert(nick,martha)
insert(martha, jayne)