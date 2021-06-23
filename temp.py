import sys
from collections import deque

numbers = [3, 30, 34, 5, 9, 31, 330, 304]
# numbers = [6,10,2]

numbers = sorted(list(map(str, numbers)), reverse = True)
length = len(numbers)
print(numbers)

if length >= 2 :
    for i in range(length) :
        idx = i
        num = numbers[idx]
        check_idx = idx -1
        while check_idx >= 0 :
            check_num = numbers[check_idx]
            if check_num.startswith(num) and len(check_num) != len(num) :
                after_string = check_num[len(num):]
                if after_string < num :
                    numbers[idx], numbers[check_idx] = numbers[check_idx], numbers[idx]
                    idx -= 1
            else :
                break
            check_idx -= 1
        print(numbers)

print(''.join(numbers))