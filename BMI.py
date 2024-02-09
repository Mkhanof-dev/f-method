weight = float(input('Please, enter your weight(kg): '))  # check user weight
height = float(input('Please, enter your height(m): '))  # check user height

while weight == 0 or height == 0:  # non-rules enter by user
    if weight == 0:
        weight = float(input('Please, enter your weight: '))
    elif height == 0:
        height = float(input('Please, enter your height: '))

BMI = weight / (height ** 2)  # Calc the BMI
Normal_BMI = 22.5

print(f"Table for your info:\nHEIGHT | {height:=6.2f}\nWEIGHT | {weight:=6}\nBMI    | {BMI:=6.1f}\nNormal | "
      f"{Normal_BMI:=6}")  # info in table-view

# BMI comment
if BMI < 20:
    print(f"Your BMI = weight / height^2 = {weight} / {height}^2 = {BMI:.1f}")
    print('It\'s very small BMI!')
elif 20 <= BMI < 25:
    print(f"Your BMI = weight / height^2 = {weight} / {height}^2 = {BMI:.1f}")
    print('It\'s normal BMI!')
elif 25 <= BMI < 30:
    print(f"Your BMI = weight / height^2 = {weight} / {height}^2 = {BMI:.1f}")
    print('It\'s overweight!')
elif 30 <= BMI < 40:
    print(f"Your BMI = weight / height^2 = {weight} / {height}^2 = {BMI:.1f}")
    print('It\'s first degree-obesity!')
elif BMI >= 40:
    print(f"Your BMI = weight / height^2 = {weight} / {height}^2 = {BMI:.1f}")
    print('It\'s very big BMI!')
else:
    print(0)
