# part 1
import re


def part_one():
    with open('input.txt') as f:
        d = f.read()

    cum = 0

    mul_regex = r'mul\(\d+\s*,\s*\d+\)'

    m = re.findall(mul_regex, d)
    if m:
        print("here's the match")
        for match in m:
            comma_separated = (match.split("mul(")[1].split(")")[0]).split(",")
            nums = [int(x) for x in comma_separated]
            cum+= nums[0] * nums[1]
    else:
        print('no match')

    print(cum)

def part_two():
    with open('input.txt') as f:
                input_text = f.read()

    mul_regex = re.finditer(r'mul\(\d+\s*,\s*\d+\)', input_text)
    do_regex = re.finditer(r'do\(\)', input_text)
    don_t_regex = re.finditer(r'don\'t\(\)', input_text)

    all_matches = []
    #
    # Merge the matches
    for match in mul_regex:
        all_matches.append((match.start(), 'mul', match.group()))
    for match in do_regex:
        all_matches.append((match.start(), 'do', match.group()))
    for match in don_t_regex:
        all_matches.append((match.start(), 'don_t', match.group()))

    # Sort the matches by the start
    all_matches.sort(key=lambda x: x[0])

    do_mul = True
    cum = 0
    for match in all_matches:
        if do_mul:
            if match[1] == 'mul':
                comma_separated = (match[2].split("mul(")[1].split(")")[0]).split(",")
                nums = [int(x) for x in comma_separated]
                cum+= nums[0] * nums[1]
            if match[1] == 'do':
                do_mul = True
            if match[1] == 'don_t':
                do_mul = False
        else:
            if match[1] == 'mul':
                continue
            if match[1] == 'do':
                do_mul = True
            if match[1] == 'don_t':
                do_mul = False
    print(cum)


print(f"Part 1 sol: + {part_one()}")
part_two()
