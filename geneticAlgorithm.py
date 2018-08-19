import readBins
import thebins
import numpy as np
import random
import chromosome
from openpyxl import Workbook

class geneticalgorithm:

    def __init__(self, iter, pop, tour, r):
        self.initialpopulation = pop
        self.tsize = tour
        self.generations = iter
        self.poplist = []
        self.parentpop = []
        self.values = r
        self.readbins = [self.values[0], self.values[1]]
        self.bins = []
        self.best = chromosome.chromosome()
        self.bestFit = 0

        for i in range(self.initialpopulation):
            cr = chromosome.chromosome()
            s = self.buildsol(cr.getsol())
            cr.setsol(s)
            self.sol(cr.getsol())
            cr.solbins = self.bins.copy()
            cr.fitness = self.fit(cr.solbins)
            self.poplist.append(cr)

    def pack(self):
        for z in range(self.generations):
            for j in self.poplist:
                j.fitness = self.fit(j.solbins)
            self.tournament()
            self.poplist = []
            for i in self.parentpop:
                r = random.randint(0, len(self.parentpop)-1)
                pa = self.parentpop[r]
                del self.parentpop[r]
                k = random.randint(0, len(self.parentpop)-1)
                pb = self.parentpop[k]
                del self.parentpop[k]
                c = self.crossover(pa, pb)
                self.sol(c.solution)
                c.solbins = self.bins.copy()
                self.poplist.append(c)
                self.poplist.append(pa)
                self.poplist.append(pb)
            for j in self.poplist:
                j.fitness = self.fit(j.solbins)
            self.selectBest()
            print("Generation ", z, ": ")
            # print("Fitness: ")
            # print(self.bestFit)
            # print("Current Best Heuristic:")
            # print(self.best.solution)
            # print("Bins :")
            # print(len(self.best.solbins))
            # print("Current Pop:")
            # print(len(self.poplist))


    def selectBest(self):
        for i in self.poplist:
            if i.fitness > self.bestFit:
                self.bestFit = i.fitness
                self.best = i

    def display(self):
        print("Best Heuristic:")
        print(self.best.solution)
        print("Fitness:")
        print(self.best.fitness)
        print("Bins:")
        print(len(self.best.solbins))

    def displayHeuristic(self):
        return self.best.solution

    def tournament(self):
        w = chromosome.chromosome()
        for i in range(10):
            for j in range(0, self.tsize):
                r = random.randint(0, len(self.poplist)-1)
                temp = self.poplist[r]
                if temp.fitness > w.fitness:
                    w = temp
            self.parentpop.append(w)

    def crossover(self, parentA, parentB):
        h = []
        h += parentA.solution[:int(len(parentA.solution)/2)]
        h += parentB.solution[int(len(parentB.solution)/2):]
        child = chromosome.chromosome()
        child.solution = h
        return child

    def buildsol(self, solution):
        r = random.randint(1, 100)
        for i in range(r):
            j = random.randint(0, 3)
            if j == 0:
                solution.append('b')
            if j == 1:
                solution.append('f')
            if j == 2:
                solution.append('w')
            if j == 3:
                solution.append('n')
        return solution

    def sol(self, h):
        k = 0
        self.bins = []
        for i in self.values[2:]:
            l = len(h)
            # print(l)
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

    def fit(self, bins):
        n = len(bins)
        c = self.readbins[1]
        f = 0
        for bin in bins:
            f = f + pow((bin.sum / c), 2)
        return f / n

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
