import numpy as np
x,y = np.random.multivariate_normal([0,0],[[1,0],[0,100]],10).T
print(x,y)
