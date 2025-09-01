A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']


def main():
    result = dict()

    for index, value in enumerate(A):
        key = B[index]
        if key in result:
            result[key] += value
        else:
            result[key] = value
    print(result)
    
if __name__ == '__main__':
    main()
