import numpy as np
from numpy import dot
from numpy.linalg import norm

userRating = np.array([
    [4.0, 2.0, 0.0, 5.0, 4.0],
    [5.0, 3.0, 4.0, 0.0, 3.0],
    [3.0, 0.0, 4.0, 4.0, 3.0]])
print(userRating)
similarityUser = np.zeros((userRating.shape[0], userRating.shape[0]))

#de xuat user gan voi user đang xet
def knn_search(D, K):
    ind = np.argpartition(D, -K)[-K:]
    return ind


for i in range(userRating.shape[0]):
    for j in range(i, userRating.shape[0]):
        a = []
        b = []
        for k in range(userRating.shape[1]):
            if userRating[i][k] != 0 and userRating[j][k] != 0:
                a.append(userRating[i][k])
                b.append(userRating[j][k])
            
        similarityUser[i][j] = dot(a, b)/(norm(a)*norm(b))
        similarityUser[j][i] = similarityUser[i][j] 

print(similarityUser)
result = userRating

for i in range(userRating.shape[0]):
    for j in range(userRating.shape[1]):
        if userRating[i][j] == 0:
            tu = 0
            mau = -1
            #tim 3 user gan tuong dong nhat voi user dang xet
            neig_idx = knn_search(similarityUser[i],3)
            print(neig_idx)
            for k in neig_idx:
                tu += similarityUser[i][k] * userRating[k][j]
                mau += similarityUser[i][k]
            print(tu/mau)
            result[i][j] = tu/mau   
print(result)
