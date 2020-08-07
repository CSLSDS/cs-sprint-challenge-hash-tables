def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    ht = {}
    for index in range(length):
        requisite = limit - weights[index]
        if requisite in ht: # second pass; ix will be the latter
            return (index, ht[requisite])
        else:
            ht[weights[index]] = index

    return None
