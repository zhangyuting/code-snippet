#!/usr/bin/env python

from foo.b import target
from foo.b import class1

def printutil():
    target()
    c = class2()
    c.class1_fun()
    print("util")


class class2(class1):
    def __init__(self):
        class1.__init__(self)
        print("From class2")
