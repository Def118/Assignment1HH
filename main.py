import readBins
import lowLevelHeuristics
import tabuSearch


def main():
    # r = readBins.readfilebin()
    # b = []
    # print("First Fit")
    # lowLevelHeuristics.first_fit(r)
    # print("Best Fit")
    # lowLevelHeuristics.best_fit(r)
    # print("Next Fit")
    # lowLevelHeuristics.next_fit(r)
    # print("Worst Fit")
    # lowLevelHeuristics.worst_fit(r)
    ts = tabuSearch.tabu()
    ts.pack(200)
    ts.display()


main()
