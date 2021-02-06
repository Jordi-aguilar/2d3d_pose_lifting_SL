# standard
import math

# 3rd party
import numpy


def normalization(Xx, Xy, Xz):
    T, n = Xx.shape
    sum0 = T * n
    sum1Xx = numpy.sum(numpy.sum(Xx))
    sum2Xx = numpy.sum(numpy.sum(Xx * Xx))
    sum1Xy = numpy.sum(numpy.sum(Xy))
    sum2Xy = numpy.sum(numpy.sum(Xy * Xy))
    sum1Xz = numpy.sum(numpy.sum(Xz)) # new
    sum2Xz = numpy.sum(numpy.sum(Xz * Xz)) # new
    mux = sum1Xx / sum0
    muy = sum1Xy / sum0
    muz = sum1Xz / sum0 # new
    sum0 = 3 * sum0
    sum1 = sum1Xx + sum1Xy + sum1Xz # Added + sum1Xz
    sum2 = sum2Xx + sum2Xy + sum2Xz # Added + sum2Xz
    mu = sum1 / sum0
    sigma2 = (sum2 / sum0) - mu * mu
    if sigma2 < 1e-10:
        simga2 = 1e-10
    sigma = math.sqrt(sigma2)
    #print(mux, muy, muz)
    #print(sigma)
    return (Xx - mux) / sigma, (Xy - muy) / sigma, (Xz - muz) / sigma # Added Yz (Xz - muz) / sigma
      


def prune(Xx, Xy, Xz, Xw, watchThis, threshold, dtype):
    T = Xw.shape[0]
    N = Xw.shape[1]
    Yx = numpy.zeros((T, N), dtype=dtype)
    Yy = numpy.zeros((T, N), dtype=dtype)
    Yz = numpy.zeros((T, N), dtype=dtype) # new
    Yw = numpy.zeros((T, N), dtype=dtype)
    for t in range(T):
        sum0 = 0
        sum1 = 0.0
        for i in watchThis:
            sum0 = sum0 + 1
            sum1 = sum1 + Xw[t, i]
        Ew = sum1 / sum0
        if Ew >= threshold:
            for i in range(N):
                Yx[t, i] = Xx[t, i]
                Yy[t, i] = Xy[t, i]
                Yz[t, i] = Xz[t, i] # new
                Yw[t, i] = Xw[t, i]
    return Yx, Yy, Yz, Yw # Added Yz


def interpolation(Xx, Xy, Xz, Xw, threshold, dtype):
    T = Xw.shape[0]
    N = Xw.shape[1]
    Yx = numpy.zeros((T, N), dtype=dtype)
    Yy = numpy.zeros((T, N), dtype=dtype)
    Yz = numpy.zeros((T, N), dtype=dtype) # new
    for t in range(T):
        for i in range(N):
            a1 = Xx[t, i]
            a2 = Xy[t, i]
            a3 = Xz[t, i] # new
            p = Xw[t, i]
            sumpa1 = p * a1
            sumpa2 = p * a2
            sumpa3 = p * a3 # new
            sump = p
            delta = 0
            while sump < threshold:
                change = False
                delta = delta + 1
                t2 = t + delta
                if t2 < T:
                    a1 = Xx[t2, i]
                    a2 = Xy[t2, i]
                    a3 = Xz[t2, i] # new
                    p = Xw[t2, i]
                    sumpa1 = sumpa1 + p * a1
                    sumpa2 = sumpa2 + p * a2
                    sumpa3 = sumpa3 + p * a3 # new
                    sump = sump + p
                    change = True
                t2 = t - delta
                if t2 >= 0:
                    a1 = Xx[t2, i]
                    a2 = Xy[t2, i]
                    a3 = Xz[t2, i] # new
                    p = Xw[t2, i]
                    sumpa1 = sumpa1 + p * a1
                    sumpa2 = sumpa2 + p * a2
                    sumpa3 = sumpa3 + p * a3 # new
                    sump = sump + p
                    change = True
                if not change:
                    break
            if sump <= 0.0:
                sump = 1e-10
            Yx[t, i] = sumpa1 / sump
            Yy[t, i] = sumpa2 / sump
            Yz[t, i] = sumpa3 / sump # new
    return Yx, Yy, Yz, Xw # Added Yz
