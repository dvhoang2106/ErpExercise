import numpy as np


#hoan thanh ma tran tu mang cho san
def complete(inputMatrix):
    length = len(inputMatrix) + 1
    # ones : tạo ma tran 1
    M1 = np.ones([length, length])
    #print(M1)
    for index, item in enumerate(inputMatrix):
        M1[index][index + 1] = item
        M1[index + 1][index] = 1.0 / item
    for i in range(0, length):
        for j in range(1, length):
            if i == j:
                continue
            if i > j:
                break
            else:
                #su dung tinh chat Aij=Aij-1*Aj-1j
                M1[i][j] = M1[i][j-1] * M1[j-1][j]
                M1[j][i] = 1.0 / M1[i][j]
    return M1



if __name__ == '__main__':
    M1 = np.array([3, 1/2, 2])
    
    M1 = complete(M1)
    print(M1) 