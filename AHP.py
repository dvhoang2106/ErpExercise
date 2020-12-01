#dau tien ta can xac dinh trong so cho cac nhan to
#sau do xac dinh diem so cho tung phuong an ung voi moi nhan to
#tiep den danh gia  phuong an bang cach nhan trong so ung voi diem so cua moi nhan to xac dịnh o buoc tren

import numpy as np
from scipy.sparse.linalg import eigs


M1 = np.array([ [1, 1.0/5.0, 3, 4], 
                [5, 1, 9, 7],
                [1.0/3.0, 1.0/9.0, 1, 2],
                [1.0/4.0, 1.0/7.0, 1.0/2.0, 1]])

price = np.array([[1, 3, 2], [1.0/3.0, 1, 1.0/5.0], [0.5, 5, 1]])
distance = np.array([[1, 6, 1.0/3.0], [1.0/6.0, 1, 1.0/9.0], [3, 9, 1]])
labor = np.array([[1, 1.0/3.0, 1], [3, 1, 7], [1, 1.0/7.0, 1]])
wage = np.array([[1, 1.0/3.0, 0.5], [3, 1, 4], [2, 0.25, 1]])

test = np.array([[1, 0.5, 3], [2, 1, 4], [1.0/3.0, 0.25, 1]])
RANDOM_INDICES = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.40, 1.45, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]


def supportFunc(M1):
    b = M1.dot(M1).sum(axis=1)# tinh tong theo hang buoc2
    return b / b.sum()# buoc3 

def findEigen(M1, epsilon=1e-5):
    M1_ = M1
    M1__ = M1.dot(M1) #binh phuong ma tran
    tmp1 = supportFunc(M1_)
    tmp2 = supportFunc(M1__)
    diff = np.abs((tmp1 - tmp2)).sum()
    while diff >= epsilon:
        M1_ = M1__
        M1__ = M1_.dot(M1_)
        tmp1 = supportFunc(M1_)
        tmp2 = supportFunc(M1__)
        diff = np.abs((tmp1 - tmp2)).sum()
    return tmp1


def findEigenUsingLib(M1):
    width = M1.shape[0]
    _, vectors = eigs(M1, k=(width-2), sigma=width, which='LM', v0=np.ones(width))
    real_vector = np.real([vec for vec in np.transpose(vectors) if not np.all(np.imag(vec))][:1])
    sum_vector = np.sum(real_vector)
    return np.around(real_vector, decimals=3)[0] / sum_vector


def finalResult(M1, distance, price, labor, wage):
    ref = ['Location A', 'Location B', 'Location C']
    M1 = findEigen(M1)
    dis = findEigen(distance)
    pri = findEigen(price)
    la = findEigen(labor)
    wa = findEigen(wage)
    matrix = np.stack((pri, dis, la, wa)).T
    result = np.round(matrix.dot(M1), decimals=3)
    for i, item in enumerate(result):
        print(f'Score for {ref[i]}: {item}')
    print(f'Recommendation is: {ref[int(np.argmax(result))]}')


def approximate(preference_matrix):
    row_sums = np.sum(preference_matrix, axis=1)
    total_sum = np.sum(row_sums)
    return row_sums / total_sum


def normalizationMatrix(preference_matrix):
    preference_matrix = preference_matrix / preference_matrix.sum(axis=0)
    preference_matrix = preference_matrix.sum(axis=1)
    return preference_matrix / preference_matrix.sum()


# Chi check neu nhu shape matrix lon hon 3
def checkCR(matrix, vector):
    # Step1: Matrix * Vector
    n = matrix.shape[0]
    if n >= 3:
        vtts = matrix.dot(vector)
        vtnq = vtts / vector
        lamdamax = np.mean(vtnq)
        #chi so phu hop lamda CR < 10% thi thoa man
        CI = (lamdamax - n)/(n - 1)
        CR = CI / RANDOM_INDICES[n - 1]
        print(f'Gia tri CR: {CR}')
        if CR < 0.1:
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    finalResult(M1, distance, price, labor, wage)
    # print(f'Test findEgien: {findEigen(test)}')
    # print(f'Test Approxmate: {approximate(test)}')
    # print(f'Test normalizationMatrix: {normalizationMatrix(test)}')
    # print(f'Check CR: {checkCR(test, findEigen(test))}')