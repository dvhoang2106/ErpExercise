import numpy as np
from scipy.sparse.linalg import eigs

def complete(M1):
    #them 1 truoc mang ban dau
    M = np.append(np.array([1]), M1)
    #tao ma tran duong cheo bang 1
    M1 = np.eye(M.shape[0])
    #bo hang dau tien ma dan M vao
    M1 = np.vstack((M, M1[1:]))

    for i in range(M1.shape[0]):     #complete  cot dau tien bang cong thuc Aij = 1 / Aji
        if M1[i][0] == 0:
            M1[i][0] = 1 / M1[0][i]

    for i in range(M1.shape[0]):    #complete  cac vi tri con lai bang cong thuc Aij*Ajk=Aik
        for j in range(i + 1, M1.shape[1]):
            if M1[i][j] == 0:
                M1[i][j] = M1[i][0] * M1[0][j]
                M1[j][i] = 1 / M1[i][j]
    return M1 
     

if __name__ == "__main__":


    # Input
    M1 = np.array([3, 1/2, 2])
    
    M1 = complete(M1)
    print(M1)              