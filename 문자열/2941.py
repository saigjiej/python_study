# 2941번 : 크로아티아 알파벳
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, 'a')
print(len(b))