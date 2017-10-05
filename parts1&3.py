# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
#part 1
print(np.zeros((4,3), dtype=np.uint16))
print(np.zeros((4,3), dtype=np.int64))
print(np.zeros((4,3), dtype=np.uint32))
print(np.zeros((4,3), dtype=np.uint64))
print(np.full((4,3), 5, dtype=np.int))
print(np.zeros((4,3), dtype=np.str))

#part 3
print(' 1 = ',min(5,8,9,3))
print(' 2 = ',max(min(5,8),max(7,3)))
print(' 3 = ',min(5,max(8,max(7,3))))
print(' 4 = ',3/5 * 3./5)
print(' 5 = ',3/(5*3.)/5)
print(' 6 = ',3/((5*3.)/5))
print(' 7 = ',3/5**2)
print(' 8 = ',3/5.**2)
print(' 9 = ',3/max(min(5**2,3),2.))
print('10 = ',3/(5.**(max(min(2,3),2.))))

