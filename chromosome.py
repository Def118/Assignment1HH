import numpy as np
import thebins
import random


class chromosome:
    def __init__(self):
        self.solution = []
        self.solbins = []
        self.fitness = 0


    def setfit(self, f):
        self.fitness = f

    def getfit(self):
        return self.fitness

    def getsol(self):
        return self.solution

    def setsol(self, s):
        self.solution = s

    def setbin(self, b):
        self.solbins = b.copy()

    def getbin(self):
        return self.solbins.copy()
