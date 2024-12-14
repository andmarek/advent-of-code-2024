from collections import defaultdict

def part_one(data):
    ret = 0
    adj_list = defaultdict(list)

    sections = data.split('\n\n')

    section_1 = sections[0]
    section_2 = sections[1]

    rules = section_1.split('\n')
    # build the adj list
    for rule in rules:
        before, after = rule.split('|')
        adj_list[int(before)].append(int(after))


    # traverse the graph
    updates = section_2.split('\n')
    for update in updates:
        valid = True
        nums = [int(x) for x in update.split(',')]
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i+1, len(nums)):
                next_num = nums[j]
                if current in adj_list[next_num]:
                    valid = False
                    break
        if valid:
            middle_number = nums[len(nums)//2]
            ret += middle_number


        print(nums)
    print(ret)

    return sections


def main():
    with open('input.txt') as f:
        d = f.read()

    print(part_one(d))

main()
