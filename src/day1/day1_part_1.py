from collections import defaultdict
with open("input.txt") as f:
    data = f.read()
left = []
right = []

similarity = 0
lines = data.split("\n")
for line in lines:
    if line != "":
        ll = line.split(" ")
        print(ll)
        left.append(ll[0])
        right.append(ll[-1])

right_count = defaultdict(int)
for n in right:
    right_count[int(n)] += 1

for l in left:
    similarity += right_count.get(int(l), 0) * int(l)
print(similarity)
