with open("input.txt", 'r') as f:
    data = f.read()

lines = data.split('\n')
        
safes = []
unsafes = []

def solve():
    for report in lines:
        levels: list[int] = report.split()

        if len(levels) == 0:
            continue

        safes.append(levels) if report_safe(levels) else unsafes.append(levels)

    for unsafe in unsafes:
        for i in range(len(unsafe)):
            new_report = unsafe[:i] + unsafe[i+1:]
            new_report_safe = report_safe(new_report)

            if new_report_safe:
                safes.append(new_report)
                break

    print(len(safes))

    

def report_safe(nums: list[int]) -> bool:
    increasing = False
    decreasing = False
    too_volatile = False

    l_index, r_index = 0, 1

    while r_index < len(nums):
        current_left = int(nums[l_index])
        current_right = int(nums[r_index])

        if current_left > current_right:
            increasing = True 
        if current_left < current_right:
            decreasing = True

        if abs(current_left - current_right) not in {1, 2, 3}:
            too_volatile = True

        l_index += 1
        r_index += 1

        if (increasing and decreasing) or too_volatile:
            return False
    return True

solve()
