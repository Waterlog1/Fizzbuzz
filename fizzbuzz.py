
for number in range(0,101):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
#Method1^
#Method2
for number in range(0,101):
    if number % 3 == 0 and number % 5 == 0:
        number= 'Fizzbuzz'
    elif number % 3 == 0:
        number= 'fizz'
    elif number % 5 == 0:
        number= 'buzz'
    print(number)