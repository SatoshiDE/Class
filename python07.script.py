#!/usr/bin/env python

import numpy as np
import matplotlib.pyplog as plt
%matpotlib inline #juyter

L = range(1000)
%timeit sq1 = [i**2 for i in L]
print (sq1)

a = np.arange(1000)
%timeit sq2 = a**2
print (sq2)

