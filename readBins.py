import numpy as np


def readfilebin(ds, binf):

    if ds == 0:
        # Dataset 1
        if binf == 1:
            # 25
            return np.loadtxt("Data/N1C1W1_A.BPP")
        if binf == 2:
            # 216
            return np.loadtxt("Data/N4C3W4_T.BPP")
        if binf == 3:
            # 277
            return np.loadtxt("Data/N4C1W1_Q.BPP")
        if binf == 4:
            # 246
            return np.loadtxt("Data/N4C1W1_M.BPP")
        if binf == 5:
            # 225
            return np.loadtxt("Data/N4C3W4_N.BPP")

    if ds == 1:
        # Dataset 2
        if binf == 1:
        # 25
            return np.loadtxt("Data/N1W1B1R0.BPP")
        if binf == 2:
        #216
            return np.loadtxt("Data/N1W3B2R8.BPP")
        if binf == 3:
        # 277
            return np.loadtxt("Data/N2W4B2R1.BPP")
        if binf == 4:
        # 246
            return np.loadtxt("Data/N4W3B1R1.BPP")
        if binf == 5:
        # 225
            return np.loadtxt("Data/N4W4B3R9.BPP")

    if ds == 2:
        # Dataset 3
        if binf == 1:
            # 56
            return np.loadtxt("Data/HARD0.BPP")
        if binf == 2:
            # 56
            return np.loadtxt("Data/HARD9.BPP")
        if binf == 3:
            # 57
            return np.loadtxt("Data/HARD1.BPP")
        if binf == 4:
            # 56
            return np.loadtxt("Data/HARD2.BPP")
        if binf == 5:
            # 55
            return np.loadtxt("Data/HARD3.BPP")






