input numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

det_A = np.linalg.det(A)

print("Determinate of A", det_A)

#the formula below
# A [a, b]
#   [c, d]
# det(A) = ad - bc
# det(A) = 2*4 - 3*1 = 8
# det(A) = 8 - 3 = 5

#this is for 3x3 matrix
B = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [0, 5, 2]
])

det_B = np linalg.det(B)

print("Determinate of B", det_B)

#the formula for matrix 3×3
# B [ a, b, c ]
#   [ d, e, f ]
#   [ g, h, i ]
# det(B) = a(ei - fh) - b(di - fg) + c(dh - eg)
# det(B) = 1(4*2 - 6*5) - 2(2*2 - 6*0) + 3(2*5 - 4*0)
#then you can solve this manually in paper, but in this case as a AI engineer I prefer you to using python.