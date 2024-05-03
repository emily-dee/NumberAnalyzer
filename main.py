user_name = input('What is your name? ')
x = 1
y = 100
analyze_again = True
valid_number = False

while analyze_again:
    user_number = int(input('Hi, ' + user_name + ', please chose a number between 1 and 100 > '))
    while valid_number == False:
        if x <= user_number <= y:
            print('Good job, ' + user_name + ', you picked number ' + str(user_number))
            valid_number = True
        else:
            user_number = int(input('"' + str(user_number) + '" is not between 1 and 100, please choose again > '))

    if user_number % 2 == 1:
        if user_number < 60:
            print(str(user_number) + ' is odd and less than 60.')
        elif user_number > 60:
            print(str(user_number) + ' is odd and greater than 60.')
    elif user_number % 2 == 0:
        if 2 <= user_number <= 24:
            print(str(user_number) + ' is even and less than 25.')
        elif 26 <= user_number <= 60:
            print(str(user_number) + ' is even and between 26 and 60 inclusive.')
        elif user_number >= 60:
            print(str(user_number) + ' is even and greater than 60.')

    try_again = input("Do you want to try again? y or n > ")
    if try_again == "y":
        valid_number = False
    else:
        analyze_again = False

print('Thanks for playing, ' + user_name + '.')