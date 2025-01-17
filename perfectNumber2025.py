#
#First Version:
def is_perfect_number(number):
    # Pozitif tam bölenlerin toplamını hesapla
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

 #####################################
#Second Version:
def perfectNumber(number):
    divisors = []
    for i in range(1,number):
        if number % i == 0:
            divisors.append(i)

    sumDivisiors = 0
    for x in divisors:
        sumDivisiors += x
    if sumDivisiors == number:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if perfectNumber(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
#####################################
#Third Version:
number = int(input("Enter a number: "))
divisors = []
for i in range(1,number):
    if number % i == 0:
        divisors.append(i)

divisors_sum = 0
for x in divisors:
    divisors_sum += x

if divisors_sum == number:
    print(f"{number} is a perfect number.")  
    
else:
    print(f"{number} is not a perfect number.")