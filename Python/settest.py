import random
words = {"hello":["hello","hallo","Bonjour","hallo"]}
print(words["hello"])
words["hello"].append("hey")
print(words["hello"])


from collections import defaultdict
d = defaultdict(list)

d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)
print(d['juices'])