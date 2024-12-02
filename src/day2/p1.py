with open("sample.txt", 'r') as f:
    data = f.read()
lines = data.split('\n')
safe_count = 0
for line in lines:
    nums = line.split()
    if len(nums) == 0:
        continue

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

        if abs(current_left - current_right) not in {1,2, 3}:
            too_volatile = True

        if (increasing and decreasing) or too_volatile:
            break

        r_index += 1
        l_index += 1

    if (increasing and decreasing) or too_volatile:
        print(f"Not safe, continuing: {nums}")
        continue
    else:
        print(f"!!!!Safe, continuing: {nums}")
        safe_count += 1
    

print(safe_count)
    


