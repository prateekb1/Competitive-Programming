# METHOD 1

group_size = int(input())
# All Rooms
rooms = list(map(int, input().split()))
# Unique Rooms
unique_rooms = set(rooms)
"""
Multiply sum of unique with group_size will give out some thing which will equal
to sum of all rooms if captain had same group size.
So minus sum of all rooms which gives one less for captain.
so divide this with group size -1 and you get the captains room number.
"""
print((sum(unique_rooms)*group_size - sum(rooms))//(group_size-1))

# METHOD 2

k = int(input())
room_number_list = list(map(int, input().split()))
d = {}
for i in room_number_list:
    if i not in d:
        d[i] = 0
    d[i] += 1
for n in d:
    if d[n] == 1:
        print(n)
        break