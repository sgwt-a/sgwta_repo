n = int(input())
ret = 0
t_prev = 0
for i in range(n):
    # get param
    t, v = map(int, input().split())

    # out water
    delta_t = t - t_prev
    # ret = 0 if ret - delta_t * 1 < 0 else ret - delta_t * 1
    ret = max(0, ret - delta_t * 1)
    # print(f"LOG: t = {t}, output = {delta_t * 1}, total = {ret}")

    # in water
    ret += v
    # print(f"LOG: t = {t}, input = {v}, total = {ret}")

    t_prev = t

print(ret)
