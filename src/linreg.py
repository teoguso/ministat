# from .stat_functions import pcc, stddev, mean
import stat_functions

def coef_b(xlist, ylist):
    """
    Calculates the b linear regression coefficient
    assuming that \hat y = a + b * xlist
    :param xlist:
    :param ylist:
    :return:
    """
    return pcc(xlist, ylist) * stddev(ylist) / stddev(xlist)


def coef_a(xlist, ylist):
    """
    Calculates the a linear regression coefficient
    assuming that \hat y = a + b * xlist
    :param xlist:
    :param ylist:
    :return:
    """
    return mean(ylist) - coef_b(xlist, ylist) * mean(xlist)


def predict(xlist, ylist):
    return coef_a(xlist, ylist) + coef_b(xlist, ylist) * xlist


