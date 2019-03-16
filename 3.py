a=int(input("Enter number of rows"))
old_list = [1]

for i in range(a):
    for _ in range(a-i) :
        print(" ",end="")
    print(*old_list)
    newlist = []
    newlist.append(old_list[0])
    for i in range(len(old_list) - 1):
        newlist.append(old_list[i] + old_list[i+1])
    newlist.append(old_list[-1])
    old_list = newlist