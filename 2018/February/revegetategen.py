import random
N = random.randint(2, 10 ** 1)
M = random.randint(1, 10 ** 1)
print(str(N) + " " + str(M))
for i in range(M):
    sd = random.choice(["S", "D"])
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p1 = random.choice(x[:N - 1])
    x.remove(p1)
    p2 = random.choice(x[:N - 1])
    print(sd + " " + str(p1) + " " + str(p2))
