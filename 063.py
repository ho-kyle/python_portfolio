Celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("%10s %10s" %("Celsius", "Fahrenheit"))
for i in range(11):
    Fahrenheit = Celsius[i] * 9 / 5 + 32
    print("%10s %10s" % (Celsius[i], Fahrenheit))
    print(type(str(Celsius[i])), type(str(Fahrenheit)))