# import numpy as np
# n = 10**6
# np.random.seed(1234)
# val  = np.random.rand(n, 2)
#
# count = 0
# for i in range(n):
#     dist = val[i][0]**2+val[i][1]**2
#     if dist<=1:
#         count+=1
#
# pi= float(count)/float(n)*4
# print("{0:.10f}".format(pi))


# # bubble sort
L=[1,3,2,5,4]
# for j in range(len(L)):
#     for i in range(len(L)-1-j):
#         if L[i] >L[i+1]:
#             L[i],L[i+1] = L[i+1], L[i]
#
# print(L)

sorted = False
while not sorted:
    for i in range(len(L)-1):
        if L[i] >L[i+1]:
            sorted = True
            L[i],L[i+1] = L[i+1], L[i]
    if not sorted:
        break
    else:
        sorted=False
print(L)

