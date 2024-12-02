with open("input.txt") as f:
    data = f.read()
left = []
right = []

lines = data.split("\n")
for line in lines:
    if line != "":
        ll = line.split(" ")
        print(ll)
        left.append(ll[0])
        right.append(ll[-1])

left_sorted = sorted(left)
right.sort()

count = 0
for l, r in zip(left_sorted, right):
    count += abs((int(l) - int(r)))
print(count)
