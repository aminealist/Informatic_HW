with open("cmake-build-debug/24.txt") as f:
    a = f.read().strip()
s = []
for i in a:
    if i == 'E':
        s.append(1)
    elif i == 'F':
        s.append(9999)
    else:
        s.append(0)
a = ""
left = 0
right = 11
sum = 0
counter = 0
while True:
    if sum < 2:
        right += 1
        sum += s[right]
    elif sum > 2:
        if right - left > 12:
            sum -= s[left]
            left += 1
        else:
            if right < len(s) - 1:
                right += 1
                sum += s[right]
            else:
                break
    else:
        if s[left] == 1 and s[right] == 1:
            counter += 1
        if right < len(s) - 1:
            sum -= s[left]
            left += 1
            right += 1
            sum += s[right]
        else:
            break
print(counter)
