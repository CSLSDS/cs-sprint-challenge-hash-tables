def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    isneg = {}
    for item in a:
        if item < 0:
            isneg[item] = True
    for item in a:
        if item >= 0 and -item in isneg:
            result.append(item)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
