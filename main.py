from Util import *
import matplotlib.pyplot as plt
import numpy as np
from model.PosFinal import *
from model.PosQ import *


def getSeqInput(x,y, T):
    input = None
    offset = T-1
    zeropads = np.zeros((offset, x.shape[1]))
    x = np.concatenate([zeropads, x], axis=0)
    for i in range(0, x.shape[0]-offset):
        temp = np.reshape(x[i:i+T, :], (1, -1,6))
        input = temp if input is None else np.concatenate([input, temp], axis=0)
    label = y[0:y.shape[0],:]
    #label = np.concatenate([np.zeros((label.shape[0],3)), label], axis=1)
    return input, label


def main():
    T = 20
    actualVel, predVel, covVel, actualPos, predPos_noCorrection = readDataMerged([0,1,2,8])
    measPos = actualPos + (np.random.rand(actualPos.shape[0], 3)-0.5)*2
    predPos = (np.concatenate([np.zeros((1,3)), measPos], axis=0))[0:actualPos.shape[0]] + predVel


    x = np.concatenate([predPos, measPos], axis=1)/1000
    y = actualPos/1000
    input, label = getSeqInput(x,y, T)

    model = getPosQ(input.shape[1:], T)
    model.load_weights('corrPosQ.h5')
    # history = model.fit(input, label, epochs=50, batch_size=1000, verbose=1, shuffle=True, validation_split=0.01)
    # loss_history = history.history["loss"]

    #model.save_weights('corrPosQ.h5')

    # plt.figure()
    # plt.plot(loss_history)
    # plt.show()

    #model.load_weights('corrPosQ.h5')
    for seq in range(0,11):
        actualVel, predVel, covVel, actualPos, predPos_noCorrection = readDataMerged([seq])
        measPos = actualPos+ (np.random.rand(actualPos.shape[0], 3)-0.5)*2
        predPos = (np.concatenate([np.zeros((1,3)), measPos], axis=0))[0:actualPos.shape[0]] + predVel
        x = np.concatenate([predPos, measPos], axis=1)/1000
        y = actualPos/1000
        input, label = getSeqInput(x,y, T)

        finalPos = model.predict(input)*1000
        plt.close('all')
        plt.figure()
        plt.plot(actualPos[:,0], actualPos[:,2], 'r')
        plt.plot(predPos_noCorrection[:,0], predPos_noCorrection[:,2], 'b')
        plt.plot(finalPos[:,3], finalPos[:,5], 'g')
        plt.plot(measPos[:,0], measPos[:,2], 'cyan')
        plt.savefig('seq_PosQ' + str(seq))
        #np.savetxt('data/seq_constQ' + str(seq) + '.txt', finalPos)
    #plt.show()




if __name__ == '__main__':
    main()
