def average(array):
    for nums in array:
        print(set(array))


# your code goes here


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    result = average(arr)
    print(result)