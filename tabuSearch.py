import thebins
import numpy as np
import readBins
import random


class tabu:

    def __init__(self, r):
        self.bins = []
        self.values = r
        self.readbins = [self.values[0], self.values[1]]
        self.tabuList = []
        self.heuristics = []
        self.assignH()
        self.sol(self.heuristics)
        self.initial = self.heuristics.copy()
        self.currenth = self.heuristics.copy()
        self.tabuList.append(self.heuristics)
        self.currentsol = self.bins.copy()
        self.fitness = self.fit()

    def sol(self, h):
        k = 0
        for i in self.values[2:]:
            l = len(h)
            if k >= l:
                k = 0
            if h[k] == "w":
                self.worst_fit(i)
            elif h[k] == "b":
                self.best_fit(i)
            elif h[k] == "n":
                self.next_fit(i)
            elif h[k] == "f":
                self.first_fit(i)
            k = k + 1

    def fit(self):
        if len(self.bins) == 0:
            return 0
        n = len(self.bins)
        c = self.readbins[1]
        f = 0
        for bin in self.bins:
            f = f + pow((bin.sum / c), 2)
        return f / n

    def pack(self, iter):
        for j in range(iter):
            self.bins = []
            self.heuristics = self.currenth.copy()
            self.move()
            hprime = self.heuristics
            print("Generation ", j, ":")
            print("Best Heuristics:")
            print(self.currenth)
            print("Current Move:")
            print(hprime)
            for i in self.tabuList:
                if i == hprime:
                    break
            self.sol(hprime)
            f = self.fit()
            if f > self.fitness:
                self.currentsol = self.bins.copy()
                self.fitness = f
                self.currenth = hprime.copy()
            self.tabuList.append(hprime)
            print("Best Fitness:")
            print(self.fitness)

    def display(self):
        print("Current Heuristic: ")
        print(self.currenth)
        print("Current Fitness: ")
        print(self.fitness)
        print("Bin Size:")
        print(len(self.currentsol))
        print("Initial heuristic:")
        print(self.initial)

    def displayHeuristic(self):
        return self.currenth

    def worst_fit(self, value):
        n = self.readbins[0]
        c = self.readbins[1]
        best = 0
        k = 0
        l = 0
        for bin in self.bins:
            if bin.sum + value <= c and (c - (bin.sum + value)) > best:
                best = c - (bin.sum + value)
                l = k
            k = k + 1
        if best != 0:
            self.bins[l].append(value)
        else:
            bin = thebins.Bin()
            bin.append(value)
            self.bins.append(bin)

    def best_fit(self, value):
        n = self.readbins[0]
        c = self.readbins[1]
        best = c
        k = 0
        l = 0
        for bin in self.bins:
            if bin.sum + value <= c and (c - (bin.sum + value)) < best:
                best = c - (bin.sum + value)
                l = k
            k = k + 1
        if best != c:
            self.bins[l].append(value)
        else:
            bin = thebins.Bin()
            bin.append(value)
            self.bins.append(bin)

    def next_fit(self, value):
        n = self.readbins[0]
        c = self.readbins[1]
        current = thebins.Bin()
        for bin in self.bins:
            current = bin
        if current.sum + value <= c and len(self.bins) != 0:
            current.append(value)
        else:
            bin = thebins.Bin()
            bin.append(value)
            self.bins.append(bin)

    def first_fit(self, value):
        n = self.readbins[0]
        c = self.readbins[1]
        for bin in self.bins:
            if bin.sum + value <= c:
                bin.append(value)
                break
        else:
            bin = thebins.Bin()
            bin.append(value)
            self.bins.append(bin)

    def move(self):
        j = random.randint(1, 4)
        print("Move Operator: ")
        if j == 1:
            print("Remove")
        if j == 2:
            print("Add")
        if j == 3:
            print("Change")
        if j == 4:
            print("Swap")
        if j == 5:
            print("Wut")

        if j == 1:
            self.removeH()
        if j == 2:
            self.addH()
        if j == 3:
            self.changeH()
        if j == 4:
            self.swapH()

    def removeH(self):
        if len(self.heuristics) < 2:
            return
        r = random.randint(0, len(self.heuristics)-1)
        for i in range(0, r):
            j = random.randint(0, len(self.heuristics)-1)
            del self.heuristics[j]

    def addH(self):
        r = random.randint(1, 20)
        for i in range(0, r):
            j = random.randint(1, 4)
            if j == 1:
                self.heuristics.append('w')
            if j == 2:
                self.heuristics.append('f')
            if j == 3:
                self.heuristics.append('b')
            if j == 4:
                self.heuristics.append('n')

    def assignH(self):
        r = 20
        for i in range(0, r):
            j = random.randint(1, 4)
            if j == 1:
                self.heuristics.append('w')
            if j == 2:
                self.heuristics.append('f')
            if j == 3:
                self.heuristics.append('b')
            if j == 4:
                self.heuristics.append('n')

    def changeH(self):
        r = random.randint(0, 5)
        for i in range(0, r):
            k = random.randint(0, len(self.heuristics)-1)
            j = random.randint(1, 4)
            if j == 1:
                self.heuristics[k] = 'w'
            if j == 2:
                self.heuristics[k] = 'f'
            if j == 3:
                self.heuristics[k] = 'b'
            if j == 4:
                self.heuristics[k] = 'n'

    def swapH(self):
        r = random.randint(0, len(self.heuristics)-1)
        k = random.randint(0, len(self.heuristics)-1)
        temp = self.heuristics[r]
        self.heuristics[r] = self.heuristics[k]
        self.heuristics[k] = temp
