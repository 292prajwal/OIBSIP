print('\nBMI Calculator\n\n')

name = input('Enter you name : ')


weight = float(input('Enter your weight in kilograms(kgs) : '))


height = float(input('Enter your height in meters(m) : '))

def bmi(wt, ht):
    bmi_val =  wt/(ht**2)
    print('\nYour BMI is {}\n'.format(bmi_val))
    
    if bmi_val < 18 :
        print(name + ', your BMI indicates Underweight.')
    elif bmi_val<25:
        print(name + ', your BMI indicates Normal')
    else:
        print(name + ', your BMI indicates Overweight')

bmi(weight,height)
