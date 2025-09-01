def get_sequence(n: int):
    res = []
    c = 0
    for i in range(1, n + 1):
        count_to_add = min(n - c, i)
        res.append(" ".join([str(i)] * count_to_add))
        c += count_to_add

    return str.join(" ", res)


def main():
    print(get_sequence(int(input("N: "))))


if __name__ == '__main__':
    main()
