def entry(n):
    if n < 0:
        print("Enter positive num of list!")
        exit()

    elif n == 0:
        print("Your list is empty??")
        exit()

    else:
        pass

    return n

def lists(n):
    list, neg_list, pos_list = [], [], []

    for i in range(0, n):
        tmp = int(input(f"Enter your {i + 1} number: "))
        list.append(tmp)

    list.sort()

    if list.count(0) == n:
        print("Your list is created only with 0! Try again!")
        exit()

    for i in list:
        if i < 0:
            neg_list.append(i)

        elif i > 0:
            pos_list.append(i)

        else:
            pass

    negative = lambda x: sum(neg_list)
    positive = lambda y: sum(pos_list)

    print(f"Sorted list = {list}")

    print("-----------------------------------------------------------------------------")

    print(f"Negative lists = {neg_list}")
    print(f"Positive lists = {pos_list}")

    print("-----------------------------------------------------------------------------")

    print(f"Negative nums sum = {negative(neg_list)}")
    print(f"Possitive nums sum = {positive(pos_list)}")

    print("-----------------------------------------------------------------------------")

    return list

lists(entry(int(input('N = '))))