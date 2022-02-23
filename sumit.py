import sys

def main():
    arr = []
    sum = 0
    for line in sys.stdin:
        if ('0' == line.rstrip()):
            arr.append(int(line))
            break
        if (int(line) > -2147483648 and int(line) < 2147483647) and (int(line) > 0):
            arr.append(int(line))
            sum += int(line)


    print("+-------------+-------------+")
    print("+Input:       +Output (sum) +")
    print("+-------------+-------------+")

    for i in range(0, len(arr)):
        if (i == 0):
            print('|{:<13}|'.format(arr[i]) + '{:<13}|'.format(sum))
        else:
            print('|{:<13}|             |'.format(arr[i]))

    print("+-------------+-------------+")

main()