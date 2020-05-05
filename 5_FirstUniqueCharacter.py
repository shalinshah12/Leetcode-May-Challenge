import collections
def firstUniqChar(s):
    s1 = collections.Counter(s)
    for index, ch in enumerate(s):
        if s1[ch]==1:
            return index
    return -1

print(firstUniqChar('loveleetcode'))
