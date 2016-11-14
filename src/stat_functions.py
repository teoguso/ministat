from math import sqrt, erf


def mean(f_list):
    """
    Computes the mean of the elements of a given list of numbers
    :param f_list:
    :return:
    """
    mysum = 0.
    for x in f_list:
        mysum += x
    return mysum / len(f_list)


def var(f_list):
    """
    Computes the variance of the elements of a given list of numbers
    :param f_list:
    :return:
    """
    mymean = mean(f_list)
    mysum = 0.
    for x in f_list:
        mysum += (mymean - x)**2
    return mysum / len(f_list)


def stddev(f_list):
    """
    Computes the standard deviation of the elements of a given list of numbers
    :param f_list:
    :return:
    """
    return sqrt(variance(f_list))


def cov(f_list1, f_list2):
    """
    Computes the covariance between two given list of numbers
    :param f_list1:
    :param f_list2:
    :return:
    """
    mysum = 0.
    mu1, mu2 = mean(f_list1), mean(f_list2)
    for x, y in zip(f_list1, f_list2):
        mysum += (x - mu1) * (y - mu2)
    return mysum / len(f_list1)


def pcc(f_list1, f_list2):
    return cov(f_list1, f_list2) / sqrt(var(f_list1) * var(f_list2))


