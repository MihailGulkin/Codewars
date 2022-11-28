def prime(N):
    A = [True] * (N + 1)
    k = 2
    while k <= N:
        if (A[k]):
            i = k * k
            while i <= N:
                A[i] = False
                i += k
        k += 1
    All = [i for i in range(2, N + 1) if A[i]]
    return All
