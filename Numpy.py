import numpy as np  

x = 26  
lst = [20, 25, 35, 30]  
arr = np.array(lst)  

res = np.where(arr == 30)  

if res[0].size == 0: 
    print("Not Found")
else:
    print("Found")

print(res)
