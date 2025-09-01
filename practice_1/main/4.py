def main():
    squares_summ = 0
    sum_of_input = 0

    while True:
        value = int(input())
        sum_of_input += value
        squares_summ += value ** 2

        if sum_of_input == 0:
            print("Summ of squares is:", squares_summ)
            return


if __name__ == '__main__':
    main()
