import numpy as np
import random

input_matrix = np.array([[3, 0, 1, 3, 1],
                         [1, 2, 4, 1, 3],
                         [3, 1, 1, 0, 1],
                         [0, 3, 5, 4, 4]]
                        )


def matrix_factorization(rating_matrix, k, beta, loop):
    num_users, num_items = rating_matrix.shape
    W = np.random.rand(num_users, k)
    H = np.random.rand(k, num_items)

    # an element in exist_ele has 3 parts (i index, j index, value)
    exist_ele = [(i, j, rating_matrix[i, j])
                 for i in range(num_users)
                 for j in range(num_items)
                 if rating_matrix[i, j] > 0
                 ]

    for i in range(loop):
        rand_ele = random.choice(exist_ele)
        r = rand_ele[2]
        r_hat = W[rand_ele[0], :].dot(
            H[:, rand_ele[1]])

        W[rand_ele[0], :] = W[rand_ele[0], :] + \
            2 * beta * (r - r_hat) * H[:, rand_ele[1]]
        H[:, rand_ele[1]] = H[:, rand_ele[1]] + \
            2 * beta * (r - r_hat) * W[rand_ele[0], :]

    print(W)
    print(H)
    print(W.dot(H).round(0))


matrix_factorization(input_matrix, 2, 0.01, 10000)