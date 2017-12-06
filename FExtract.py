import numpy as np


# simple moving average
def calcSma(data, smaPeriod):
    sma = []
    count = 0
    for i in range(data.size):
        if data[i] is None:
            sma.append(None)
        else:
            count += 1
            if count < smaPeriod:
                sma.append(None)
            else:
                sma.append(np.mean(data[i-smaPeriod+1:i+1]))

    return np.array(sma)


