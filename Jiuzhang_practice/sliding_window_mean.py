L= [1.0,2.0,3.0,4.0,5.0,6.0 ]
k=3

def sliding_window_mean(L, k):
    res = []
    temp = 0
    for i in range(len(L)):
        if i <= k-1:
            temp += L[i]/float(k)
            if i == k-1:
                res.append(temp)
        else:
            val = res[-1]-L[i-k]/float(k)+L[i]/float(k)
            res.append(val)
    return res

print(sliding_window_mean(L, k))

