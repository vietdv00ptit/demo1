# import numpy as np
# matrix_list =[[1,0,3],[5,6,4]]
# matrix=np.array(matrix_list)
# matrix_invert=np.linalg.pinv(matrix)
# print(matrix,'\n',matrix_invert)
# matrix_all=matrix@matrix_invert
# print(matrix_all)

# for i in range(np.size(matrix_all,0)):
#     for j in range(np.size(matrix_all,1)):
#         matrix_all[i,j]=int(matrix_all[i,j])
# print(matrix_all)



import numpy as np
import matplotlib.pyplot as plt
X=np.loadtxt('data/univariate.txt',delimiter=',')
Theta = np.loadtxt('data/univariate_theta.txt',delimiter=',')
y = np.copy(X[:,1])
X[:,1]=X[:,0]
X[:,0]=1
#Tính lợi nhuận (đơn vị 10000$)
predict = X @ Theta
#Chuyển lợi nhuận về đơn vị $
predict = 10000 * predict
#in cặp dân số-lợi nhuận đầu tiên (đơn vị dân số: người)
print('%d người : %.2f$' %(X[0,1]*10000,predict[0]))

#Plot giá trị thực tế (không lấy cột bias 1 đầu)
#X[:,1:] là x-axis của biểu đồ, không lấy cột đầu; y là y-axis, rx là red x, plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:,1],y,'rx')
#Plot dự đoán
plt.plot(X[:,1],predict/10000,'-b')#ta dùng đơn vị gốc là 10000$, -b là đường thẳng màu xanh
#show kết quả
plt.show()
#Lưu kết quả
np.savetxt('value/univariate_predicted.txt',predict,fmt = '%.6f')