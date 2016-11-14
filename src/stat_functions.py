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
    """
    Computes the Pearson correlation coefficient.
    :param f_list1:
    :param f_list2:
    :return:
    """
    return cov(f_list1, f_list2) / sqrt(var(f_list1) * var(f_list2))


def rank(f_list, unique=False):
    """
    Computes the rank of a given list.
    Parts arbitrarily extracted from stackoverflow.
    :param f_list:
    :param unique:
    :return:
    """
    if unique:
        index = range(1,len(f_list)+1)
        mydict = dict(zip(f_list, index))
        return [int(mydict[x]) for x in sorted(mydict.keys())]
    elif len(f_list) == len(set(f_list)):
        return rank(f_list, unique=True)
    else:
        n = len(f_list)
        ivec = rank(a, unique=True)
        svec = [a[irank] for irank in ivec]
        sumranks = 0
        dupcount = 0
        newlist = [0] * n
        for i in range(n):
            sumranks += i
            dupcount += 1
            if i == n - 1 or svec[i] != svec[i + 1]:
                averank = sumranks / dupcount + 1
                for j in range(i - dupcount + 1, i + 1):
                    newlist[ivec[j]] = int(averank)
                sumranks = 0
                dupcount = 0
        return newlist


def srcc(f_list1, f_list2):
    """
    Computes the Spearman's rank correlation coefficient.
    :param f_list1:
    :param f_list2:
    :return:
    """
    r1, r2 = rank(f_list1), rank(f_list2)
    n = len(f_list1)
    duplicates = (n != len(set(f_list1))) or (len(f_list2) != len(set(f_list2)))
    if duplicates:
        return pcc(r1, r2)
    else:
        d2 = 0
        for x, y in zip(r1, r2):
            d2 += (x - y)**2
        return 1 - 6 * d2 / n / (n**2 - 1)


