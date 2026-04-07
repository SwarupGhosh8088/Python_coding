import numpy as np

x = 26
lst = [20, 25, 35, 30]
arr = np.array(lst)

nearest = arr[np.abs(arr - x).argmin()]

print("Nearest value:", nearest)
