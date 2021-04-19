# Binary Search vs Naive Search
# which is better?

# Naive search
# Comapers target to list
# return -1 if yes == return index
def naive_search(l, target):
    # example l = [1, 3, 12, 16]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary search
# diveds and conquers


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return-1

    # example l = [1, 3, 12, 16]
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
