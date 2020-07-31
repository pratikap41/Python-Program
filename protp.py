if __name__ == '__main__':
    def nothing(s):
        if  s.isalpha():
            return s
        if s.isdigit():
            return int(s)




    N = int(input())
    list1 = []
    for i in range(N):

        user_input = list(map(nothing , input().split()))

        if user_input[0] == 'insert' :
            list1.insert(user_input[1], user_input[2])
        elif user_input[0] == 'print':
            print(list1)
        elif user_input[0] == 'remove' :
            list1.remove(user_input[1])
        elif user_input[0] == 'append' :
            list1.append(user_input[1])
        elif user_input[0] == 'sort' :
            sorted(list1)
        elif user_input[0] == 'pop' :
            list1.pop()
        elif user_input[0] == 'reverse' :
            print(list1[::-1])
        else:
            None



