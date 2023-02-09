height , length = 7, 21 # 11, 33
for i in range(0, height//2):
    s = '.|.'*(i * 2 + 1)
    print(s.center(length,'-'))
print('WELCOME'.center(length, '-'))
for i in range(height // 2 - 1, -1, -1):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))