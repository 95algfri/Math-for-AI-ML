import numpy as np

#nendefinisikan Vektor A dan B
A = np.array([2, 3, 5, 1, 8])
B = np.array([-1, 3, -2, 4, 7])

vector_addition(A + B)
print('A + B =', vector_addition)

#scalar_multiplication
scalar_mult(4 * A)
print("4 * A =", Scalar_mult)

#cross product multiplication AKA outer product
outer_product = np.outer(A, B)
print("A × B =", outer_product)
#Dalam AI, skala vektor biasanya dilakukan untuk menyesuaikan relevansi.
#Misalnya, jika kita melakukan perkalian produk skalar suatu vektor dengan 100, itu berarti kita meningkatkan nilainya. Jika jumlahnya 0,3, berarti kita mengurangi jumlahnya.

#dot product multiplication 
dot_product = no dot(A, B)
print("A • B =", dot_product)
#kode ini digunakan ketika kita ingin mengukur kesamaan, atau keselarasan antara dua vektor.
