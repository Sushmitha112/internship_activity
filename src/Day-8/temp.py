import numpy as np
a=np.array([])
b=np.array([10,20,30])
c=np.array([10,20,30],[40,50,60]])
d=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a,"\n",b,"\n",c,"\n",d)

arr = np.random.rand(10)
# Vectorized
squared = arr ** 2
print(squared)

arr = np.arange(12)
print(arr)
reshaped = arr.reshape(2, 6)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
hstacked = np.hstack((a, b))
print(vstacked) 
print(hstacked)

data = np.array([[10, 20, 30],
                  [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))

#task-1
arr=np.random.randint(50,100,size=(5,3))
print("original array:",arr)
mean_arr=np.mean(arr,axis=0)
print("the mean for each subject :",mean_arr)
print("the mean array from the original scores array using broadcasting",arr-mean_arr)
#task-2
arr=np.arange(0,24)
print("original array:",arr)
print("reshaped array:",arr.reshape(4,3,2))
print("transposed array:",arr.reshape(4,3,2).transpose(1,0,2))