import numpy as np
import math

rows, cols = (1, 8) # 1 x 8 vector for One ADC conververters of size 8
arr = np.zeros((rows, cols))
print(np.size(arr), np.shape(arr))
print(np.size([[0,0,0,0,0,0,0,0]]), np.shape([[0,0,0,0,0,0,0,0]]))
arr = np.append(arr,[[0,0,0,1,0,0,0,0]], axis=0)
print(np.size(arr, axis=0), np.shape(arr), arr[1,7])
arr = np.delete(arr, 0, 0)
print(np.size(arr, axis=0), np.shape(arr), arr)
exit()
