class Pell:
    def get(self, n):
        p_list = [0, 1, 2]
        a = 1
        b = 2
        while len(p_list) <= n + 1:
            p_list.append(2 * p_list[b] + p_list[a])
            a += 1
            b += 1
        return p_list[n]
