import random


def binary_search_with_loop(data, target):
    data.sort()
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1


def binary_search_with_recursion(data, target, low, high):
    data.sort()
    if low > high:
        return False

    mid = (low - high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search_recursive(data, target, low, mid - 1)
    else:
        return binary_search_recursive(data, target, mid + 1, high)


if __name__ == "__main__":
    data = [random.randint(0, 100) for i in range(10)]

    target = int(input("What number would you like to find?"))

    found_with_recursive = binary_search_recursive(
        data, target, 0, len(data - 1))

    found_with_loop = binary_search_loop(data, target)
