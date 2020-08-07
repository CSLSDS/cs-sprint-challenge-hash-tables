# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    ht = {}
    
    for f in files:
        tail = f.rpartition('/')[2]
        if tail not in ht:
            ht[tail] = []
        ht[tail].append(f)
    result = []
    for query in queries:
        if query in ht:
            result += ht[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))


    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    result = finder(files, queries)
    result.sort()

    print(result)

    print(['/dir256/dirb256/file256',
        '/dir256/file256', '/dir3490/dirb3490/file3490',
        '/dir3490/file3490', '/dir8192/dirb8192/file8192',
        '/dir8192/file8192'])