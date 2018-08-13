import numpy as np


class Bin(object):
    """ Container for items that keeps a running sum """

    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))


def first_fit(readbins):
    n = readbins[0]
    c = readbins[1]
    bins = []
    for i in range(2, int(n)):
        for bin in bins:
            if bin.sum + readbins[i] <= c:
                bin.append(readbins[i])
                break
        else:
            bin = Bin()
            bin.append(readbins[i])
            bins.append(bin)
    print(len(bins))


def best_fit(readbins):
    n = readbins[0]
    c = readbins[1]
    best = c
    k = 0
    l = 0
    bins = []
    for i in range(2, int(n)):
        k = 0
        best = c
        for bin in bins:
            if bin.sum + readbins[i] <= c and (c - (bin.sum + readbins[i])) < best:
                best = c - (bin.sum + readbins[i])
                l = k
            k = k + 1
        if best != c:
            bins[l].append(readbins[i])
        else:
            bin = Bin()
            bin.append(readbins[i])
            bins.append(bin)
    print(len(bins))


def worst_fit(readbins):
    n = readbins[0]
    c = readbins[1]
    best = 0
    k = 0
    l = 0
    bins = []
    for i in range(2, int(n)):
        k = 0
        best = 0
        for bin in bins:
            if bin.sum + readbins[i] <= c and (c - (bin.sum + readbins[i])) > best:
                best = c - (bin.sum + readbins[i])
                l = k
            k = k + 1
        if best != 0:
            bins[l].append(readbins[i])
        else:
            bin = Bin()
            bin.append(readbins[i])
            bins.append(bin)
    print(len(bins))


def next_fit(readbins):
    n = readbins[0]
    c = readbins[1]
    k = 0
    bins = []
    bin = Bin()
    bin.append(0)
    bins.append(bin)
    for i in range(2, int(n)):
        if bins[k].sum + readbins[i] <= c:
            bins[k].append(readbins[i])
        else:
            bin = Bin()
            bin.append(readbins[i])
            bins.append(bin)
            k = k + 1
    print(len(bins))