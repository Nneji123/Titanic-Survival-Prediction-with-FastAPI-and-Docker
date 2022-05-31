x = [1,2,34,3,2,43,4,3,2,3,4,2,343]
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        # find the highest common factor
        while x[i] % x[j] != 0:
            x[i] -= 1
            print(x)
        # find the lowest common multiple
        while x[j] % x[i] != 0:
            x[j] += 1
            print(x)