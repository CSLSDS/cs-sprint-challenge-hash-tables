def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    encountered = {}
    for array in arrays:
        for item in array:
            if item in encountered:
                encountered[item] += 1
            else:
                encountered[item] = 1
    for item in encountered:
        # if num counted == num of arrays
        if encountered[item] == len(arrays):
            result.append(item)
            
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
