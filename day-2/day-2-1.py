valid = 0
with open('input', 'r') as f:
    for line in f:
        r, p = line.split(': ')
        mm, l = r.split(' ')
        mi, ma = mm.split('-')
        mi = int(mi)
        ma = int(ma)
        c = p.count(l)
        if mi <= c <= ma:
            valid += 1
print(valid)
