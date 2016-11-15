from stat_funcs import pcc, stddev, mean


def main():
    from sys import stdin
    n = 5
    x, y = [], []
    for line in stdin:
        try:
            a, b = line.strip().split()
        except:
            break
        x.append(int(a))
        y.append(int(b))
    x_given = 80
    print("{:.3f}".format(predict_single(x_given, x, y)))

# def predict(mat1, )

from sklearn import linear_model

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


def predict_single(x_given, xlist, ylist):
    return coef_a(xlist, ylist) + coef_b(xlist, ylist) * x_given


if __name__ == "__main__":
    main()


