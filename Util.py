import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import minmax_scale


def readDataMerged(seqList):
    actualVel=None
    predVel=None
    covVel=None
    actualPos=None
    predPos_noCorrection=None
    for seq in seqList:
        actualVel_ind, predVel_ind, covVel_ind, actualPos_ind, predPos_noCorrection_ind = readData(seq)

        actualVel = actualVel_ind if actualVel is None else np.concatenate([actualVel, actualVel_ind], axis=0)
        predVel = predVel_ind if predVel is None else np.concatenate([predVel, predVel_ind], axis=0)
        covVel = covVel_ind if covVel is None else np.concatenate([covVel, covVel_ind], axis=0)
        actualPos = actualPos_ind if actualPos is None else np.concatenate([actualPos, actualPos_ind], axis=0)
        predPos_noCorrection = predPos_noCorrection_ind if predPos_noCorrection is None else np.concatenate([predPos_noCorrection, predPos_noCorrection_ind], axis=0)
    return actualVel, predVel, covVel, actualPos, predPos_noCorrection


def readData(seq):
    actualVel = pd.read_csv('data/actual' + str(seq) + '.txt', sep=" ", header=None).as_matrix()
    predVel = pd.read_csv('data/pred' + str(seq) + '.txt', sep=" ", header=None).as_matrix()
    covVel = pd.read_csv('data/cov' + str(seq) + '.txt', sep=" ", header=None).as_matrix()

    actualPos = vel2pos(actualVel)
    predPos_noCorrection_ind = vel2pos(predVel)
    return actualVel, predVel, covVel, actualPos, predPos_noCorrection_ind

def pos2vel(pos):
    vel = np.zeros_like(pos)
    for i in range(1, len(pos)-1):
        vel[i] = (pos[i+1]-pos[i-1])/2
    return vel

def vel2pos(vel):
    pos = np.zeros_like(vel)
    for i in range(1, len(vel)):
        pos[i] = pos[i-1] + vel[i]
    return pos

if __name__ == '__main__':
    readData(0)
