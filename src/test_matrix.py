import numpy as np 
from scipy.sparse import csr_matrix
#Esta es la primera versión en git

indptr = np.array([0, 2, 3, 6])
indices = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])

m_one = csr_matrix((data, indices, indptr), shape=(3, 3))
m_one_arr = m_one.toarray()
print(m_one_arr)

"""
[[1 0 2]
 [0 0 3]
 [4 5 6]]

"""

list_1 = [1, 3, 5, 7]
list_2 = [1, 2, 3, 5, 8, 13]

row_1 = m_one.getrow(0)
print(row_1)