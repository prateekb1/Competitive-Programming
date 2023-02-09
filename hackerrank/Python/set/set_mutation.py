def handler(a):
    command = input().split()[0]
    new_set = set(map(int,input().split()))
    if command == 'intersection_update':
        a.intersection_update(new_set)
    elif command == 'update':
        a.update(new_set)
    elif command == 'difference':
        a.difference(new_set)
    elif command == 'symmetric_difference':
        a.symmetric_difference(new_set)
    
_, a = input(), set(map(int,input().split()))
for i in range(int(input())):
    handler(a)

print(sum(a))