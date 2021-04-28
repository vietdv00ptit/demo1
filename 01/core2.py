import numpy as np
import matplotlib.pyplot as plt
X=np.loadtxt('data/multivariate.txt',delimiter=',')
Theta=np.loadtxt('data/multivariate_theta.txt',delimiter=',')
X[:,1:]=X[:,0:2]
X[:,0]=1

plt.plot(X[])

predict=X @ Theta
X[:,0:2]=X[:,1:]
X[:,2]=predict
print('%.2f feet-vuong,%d phong ngu: %d$' %(X[0,0],X[0,1],X[0,2]))
np.savetxt('value/multivariate_predict.txt',X[:,2],fmt = '%d')
