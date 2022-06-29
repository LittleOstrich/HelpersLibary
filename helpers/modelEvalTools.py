import numpy as np
from sklearn.metrics import f1_score, accuracy_score

from statsmodels.formula.api import ols


def computeFscore(y_true, y_pred, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn'):
    score = f1_score(y_true=y_true, y_pred=y_pred, labels=labels,
                     pos_label=pos_label, average=average,
                     sample_weight=sample_weight,
                     zero_division=zero_division)
    return score


def computeAccuracy(y_true, y_pred, *, normalize=True, sample_weight=None):
    score = accuracy_score(y_true, y_pred,
                           normalize=normalize,
                           sample_weight=sample_weight)
    return score


def computeConfusionLabels(y_true, y_pred):
    l = list()

    N = len(y_true)
    for i in range(N):
        yGt = y_true[i]
        yPt = y_pred[i]

        if yGt == 1 and yPt == 1:
            l.append("TP")
        elif yGt == 0 and yPt == 1:
            l.append("FP")
        elif yGt == 1 and yPt == 0:
            l.append("FN")
        elif yGt == 0 and yPt == 0:
            l.append("TN")
        else:
            assert False
        return l


def splitConfusionLabels(confusionLabels):
    TP, FP, FN, TN = 0, 0, 0, 0

    N = len(confusionLabels)
    for i in range(N):
        lbl = confusionLabels[i]
        if lbl == "TP":
            TP = TP + 1
        elif lbl == "FP":
            FP = FP + 1
        elif lbl == "FN":
            FN = FN + 1
        elif lbl == "TN":
            TN = TN + 1
        else:
            assert False
    return TP, FP, FN, TN


def computeRSquared(y_true, y_pred):
    SSE = np.sum(np.square(y_true - y_pred))
    SST = np.sum(np.square(y_true - np.mean(y_pred)))

    R = 1 - SSE / SST
    return R


def computeAdjustedRsquaredVal(y_true, y_pred, n, p):
    RSquared = computeRSquared(y_true, y_pred)
    adjustedRSquared = 1 - (1 - RSquared) * ((n - 1) / (n - p - 1))

    # return adjustedRSquared
