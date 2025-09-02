def main():
    data = dict()
    n = int(input())
    for _ in range(n):
        name = input()
        if name not in data:
            data[name] = 0
            print("OK")
        else:
            data[name] += 1
            print(f"{name}{data[name]}")

if __name__ == "__main__":
    main()
