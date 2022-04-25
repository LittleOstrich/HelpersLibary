import numpy as np
import scipy.constants

c = scipy.constants.c
pi = scipy.constants.pi
k = scipy.constants.k


class pQ:
    numericalValue = None
    SI_Unit = None
    prefix = None


class scales:
    nano = "nano"
    micro = "micro"
    milli = "milli"
    default = ""
    kilo = "kilo"
    mega = "mega"
    giga = "giga"

    auto = "auto"


def mag(num):
    digits = None
    if np.abs(num) >= 1:
        digits = int(np.log10(num)) + 1
    else:
        pass
    if digits > 11:
        assert False
    return digits


def reScale(res, scale=scales.auto):
    f = None
    unit = None
    if scale == scales.nano:
        f = 10 ** -9
        unit = scales.nano
    elif scale == scales.micro:
        f = 10 ** -6
        unit = scales.micro
    elif scale == scales.milli:
        f = 10 ** -3
        unit = scales.milli
    elif scale == scales.kilo:
        f = 10 ** 3
        unit = scales.kilo
    elif scale == scales.mega:
        f = 10 ** 6
        unit = scales.mega
    elif scale == scales.giga:
        f = 10 ** 9
        unit = scales.giga
    elif scale == scales.auto:
        numDigits = mag(res)
        if numDigits in [3, 4, 5]:
            res, unit = reScale(res, scales.kilo)
        elif numDigits in [6, 7, 8]:
            res, unit = reScale(res, scales.mega)
        elif numDigits in [9, 10, 11]:
            res, unit = scales.giga = reScale(res, scales.giga)
        else:
            assert False
        return res, unit
    res = res / f
    return res, unit


def computeDiff_fnat(tau1, tau2):
    diff_f_nat = (1 / (2 * pi)) * (1 / tau1 + 1 / tau2)
    diff_f_nat, unit = reScale(diff_f_nat)
    return diff_f_nat, unit


tau1 = 100 * 10 ** -9
tau2 = 9.8 * 10 ** -9
res, unit = computeDiff_fnat(tau1, tau2)
res, unit = reScale(res, scales.mega)
print(res)


def computeDopplerProfile(f0, T, m):
    res = 2 * f0 / c * np.sqrt((2 * k * T * np.log(2)) / m)
    res, unit = reScale(res)
    return res, unit


# lambda1 = 632.8 * 10 ** -9
# T = 500
# m = 3.35 * 10 ** -26
# res = computeDopplerProfile(c / lambda1, T, m)
# print(res)

lambda1 = 10.6 * 10 ** -6
T = 500
m = 44 * 10 ** -27
print(c / lambda1)
res, unit = computeDopplerProfile(28000000000000, T, m)
print(res, unit)
