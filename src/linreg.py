# from .stat_functions import pcc, stddev, mean
from stat_funcs import pcc, stddev, mean


def main():
    from sys import stdin
    n = 5
    math, stat = [], []
    for line in stdin:
        a, b = line.strip().split()
        math.append(int(a))
        stat.append(int(b))
    x_given = 80
    print("{:.3f}".format(predict(x_given, math, stat)))


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


def predict(x_given, xlist, ylist):
    return coef_a(xlist, ylist) + coef_b(xlist, ylist) * x_given


if __name__ == "__main__":
    main()


