height = eval(input('請輸入身高(公分): '))
weight = eval(input('請輸入體重(公斤): '))
BMI = weight / (height / 100)**2
if BMI < 18.5:
    print(f'{BMI = :5.2f}體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print(f'{BMI = :5.2f}正常')
elif BMI >= 24 and BMI < 28:
    print(f'{BMI = :5.2f}超重')
elif BMI >= 28:
    print(f'{BMI = :5.2f}肥胖')