class Primes:
    @staticmethod
    def stream():
        limit = 16_000_000
        p = [True] * limit
        for i in range(2, int(limit ** 0.5 + 1)):
            if p[i]:
                p[i * 2:limit:i] = [False] * ((limit + i - 1) // i - 2)
        p[0] = p[1] = False
        p = (p_num for p_num, is_prime in enumerate(p) if is_prime)
        for num in p:
            yield num
