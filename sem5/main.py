import time

def bin_search(arr, x):
    n = len(arr)
    
    if n == 1:
        if x == arr[n // 2]:
            return True
        else:
            return False
    if x == arr[n // 2]:
        return True
    elif x > arr[n // 2]:
        return bin_search(arr[n // 2 + 1:], x)
    elif x < arr[n // 2]:
        return bin_search(arr[:n // 2], x)


def bin_search_2(arr, x):
    n = len(arr)
    l, m, r = 0, n // 2, n
    
    while arr[m] != x:
        if x < arr[m]:
            r = m
        else:
            l = m + 1
        m = (r + l) // 2
        
        if r - l == 1 or arr[m] == x:
            break
        
    #if arr[m] == x:
    #    print(f'x is found at i = {m}')
    return m


def bin_search_LIS(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

'''
A = [1, 3, 5, 7, 8, 9, 10]
x = 9

print(bin_search(A, x))
print(bin_search_2(A, x))
'''

def lis_n2(arr): # longest increasing subsequence
    n = len(arr)
    
    dp = [1 for _ in range(n)] # длина наибольшей подпоследовательности, оканчивающейся на arr[i]
    
    for i in range(1, n):
        max_dp = float('-inf')
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] > max_dp:
                max_dp = dp[j]
        dp[i] = 1 + max_dp
    
    return max(dp)

def LIS_nlogn(arr):
    n = len(arr)
    dp = [float('inf') for i in range(n+1)]
    dp[0] = float('-inf')
    res = 0
    for x in arr:
        k = bin_search_LIS(dp, x)
        if dp[k - 1] < x < dp[k]:
            dp[k] = x
            res = max(res, k)

    return res




C = [i for i in range(30000)]

'''
t = time.time()
print(lis_n2(C))
print(time.time() - t)

t = time.time()
print(LIS_nlogn(C))
print(time.time() - t)
'''

def fastpow(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        return fastpow(a, n // 2) ** 2
    else:
        return a * fastpow(a, (n - 1))
    
print(fastpow(10, 10))


