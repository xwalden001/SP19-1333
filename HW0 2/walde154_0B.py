def numReverse(num):
    if type(num) == int and len(str(num)) == 3:
        num = int(num)
        last = num//100
        remain = num%100
        middle = remain//10
        first = remain%10

        if middle == 0 and first == 0:
            print(str(last))
        else:
            print(str(first)+str(middle)+str(last))
    else:
        print("None")


def main():
    num = 215#input("Enter 3 Digit Number: ")
    numReverse(num)
    num = 200#input("Enter 3 Digit Number: ")
    numReverse(num)
    num = 201#input("Enter 3 Digit Number: ")
    numReverse(num)

if __name__ == '__main__':
    main()
