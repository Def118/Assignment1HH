import readBins
import lowLevelHeuristics
import tabuSearch
import geneticAlgorithm
from openpyxl import Workbook
import time
from functools import reduce

def main():
    book = Workbook()
    tabuSheet = book.active
    gaSheet = book.create_sheet()
    for v in range(0, 3):
        ret = [0, 0, 0, 0, 0, 0, 0]
        tabuSheet.append(ret)
        gaSheet.append(ret)
        for k in range(1, 6):
            for i in range(1):
                r = readBins.readfilebin(v, k)
                print(v, " - ", k)
                print("==============================")
                print("First Fit")
                lowLevelHeuristics.first_fit(r)
                print("Best Fit")
                lowLevelHeuristics.best_fit(r)
                print("Next Fit")
                lowLevelHeuristics.next_fit(r)
                print("Worst Fit")
                lowLevelHeuristics.worst_fit(r)
                print("==============================")

        #     r = readBins.readfilebin(v, k)
        #     ret = [0, 0, 0, 0, 0, 0, 0]
        #     ave = []
        #     b = []
        #     start = time.clock()
        #     for i in range(30):
        #         ts = tabuSearch.tabu(r)
        #         ts.pack(500)
        #         test = tallyheuristic(ts.displayHeuristic())
        #         for j in range(0, 4):
        #             ret[j] = ret[j] + test[j]
        #         ave.append(ts.fitness)
        #         b.append(len(ts.currentsol))
        #         # ts.display()
        #     end = time.clock()
        #
        #     ret[4] = reduce(lambda x, y: x + y, ave) / len(ave)
        #     ret[5] = reduce(lambda x, y: x + y, b) / len(b)
        #     ret[6] = end - start
        #     showAve(ret)
        #     tabuSheet.append(ret)
        #
        #     ret = [0, 0, 0, 0, 0, 0, 0]
        #     ave = []
        #     b = []
        #
        #     start = time.clock()
        #     for i in range(30):
        #         ga = geneticAlgorithm.geneticalgorithm(500, 30, 10, r)
        #         ga.pack()
        #         # ga.display()
        #         test = tallyheuristic(ga.displayHeuristic())
        #         for j in range(0, 4):
        #             ret[j] = ret[j] + test[j]
        #         ave.append(ga.bestFit)
        #         b.append(len(ga.best.solbins))
        #
        #     end = time.clock()
        #
        #     ret[4] = reduce(lambda x, y: x + y, ave) / len(ave)
        #     ret[5] = reduce(lambda x, y: x + y, b) / len(b)
        #     ret[6] = end - start
        #     showAve(ret)
        #     gaSheet.append(ret)
        #
        # book.save('bins.xlsx')


def tallyheuristic(h):
    ret = [0, 0, 0, 0]
    for i in h:
        if i == 'b':
            ret[0] = ret[0] + 1
        if i == 'f':
            ret[1] = ret[1] + 1
        if i == 'w':
            ret[2] = ret[2] + 1
        if i == 'n':
            ret[3] = ret[3] + 1
    return ret


def showAve(h):
    print("Best fit:")
    print(h[0])
    print("First fit:")
    print(h[1])
    print("Worst fit:")
    print(h[2])
    print("Next fit")
    print(h[3])


main()
