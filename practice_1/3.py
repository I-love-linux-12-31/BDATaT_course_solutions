def main():
    data = dict()
    n = int(input())
    for i in range(n):
        file, *mode = input().split()
        data[file] = mode
    m = int(input())

    for i in range(m):
        op, file = input().split()
        op = {"write": "w", "read": "r", "execute": "x"}[op]
        if op in data[file]:
            print("OK")
        else:
            print("Access denied")


if __name__ == "__main__":
    main()
