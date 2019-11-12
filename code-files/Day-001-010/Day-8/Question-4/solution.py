import collections
def migratoryBirds(arr):
    return (sorted(dict(collections.Counter(arr)).items(), key = lambda kv: kv[1]).pop()[0])
migratoryBirds(arr = list(map(int, input().rstrip().split())))