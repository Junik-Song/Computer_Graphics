import numpy as np

# A. Create a 1d array M with values ranging from 2 to 26 and print M.
M=np.array([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])

print(M,"\n")

# B. Reshape M as a 5x5 matrix and print M. 
M = np.reshape(M, (5,5))

print(M,"\n")


# C. Set the first column of the matrix M to 0 and print M.

M[:,0] = 0

print(M,"\n")



# D. Assign M2 to the M and print M.
M=M@M

print(M,"\n")

# E. Now, let’s consider the first row of matrix M as vector v. 
# Calculate the magnitude of the vector v and print it.

v=M[0,:]

mag=0
for i in v:
    mag=mag+i*i;


mag=np.sqrt(mag);

print(mag,"\n")
