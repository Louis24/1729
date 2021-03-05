# 1729
def main():
    i = 1

    while True:
        print(i)
        n = 1729 * i * i + 1
        if isSqr(n):
            print(i, n)
            return
        else:
            i += 1
