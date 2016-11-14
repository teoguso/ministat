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


def variance(f_list):
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



