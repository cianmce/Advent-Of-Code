
data = ''
with open('input.txt') as f:
    data = f.read()

count = 0

for i in range(len(data)):
    if data[i]=='(':
        count += 1
    else:
        count -= 1
    if count < 0:
        print i+1
        break
