import textdistance


class stringMetrics:
    hamming = "hamming"
    levenshtein = "levenshtein"
    jaroWinkler = "jaroWinkler"
    needlemanWunsch = "needlemanWunsch"
    gotoh = "gotoh"
    smithWaterman = "smithWaterman"


def getMetric(metric):
    m = None
    if metric == stringMetrics.levenshtein:
        m = textdistance.levenshtein(external=False)
    elif metric == stringMetrics.hamming:
        m = textdistance.hamming(external=False)
    elif metric == stringMetrics.gotoh:
        m = textdistance.gotoh(external=False)
    elif metric == stringMetrics.smithWaterman:
        m = textdistance.smith_waterman(external=False)
    elif metric == stringMetrics.jaroWinkler:
        m = textdistance.jaro_winkler(external=False)
    elif metric == stringMetrics.needlemanWunsch:
        m = textdistance.needleman_wunsch(external=False)
    else:
        print("Unknown string metric!: ", metric)
        assert False
    return m


def cleanString(s: str, removees=None):
    if removees is None:
        removees = ",;[](){}\n"

    for r in removees:
        s = s.replace(r, "")
    return s


def compareLists(A, B, threshold, metric):
    N = len(A)
    M = len(B)

    for i in range(N):
        s1 = A[i]
        for j in range(M):
            s2 = B[j]
