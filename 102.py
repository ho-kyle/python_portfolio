teaPerTab = 3
teaPerCup = 48

def volume(unitNumber, measureUnit):
    measureUnit = measureUnit.lower()
    if measureUnit == 'teaspoon' or measureUnit == 'teaspoons':
        teaspoon = unitNumber
    if measureUnit == 'cup' or measureUnit == 'cups':
        teaspoon = unitNumber * teaPerCup
    if measureUnit == 'tablespoon' or measureUnit == 'tablespoons':
        teaspoon = unitNumber * teaPerTab
    result = ''
    cup = teaspoon // teaPerCup
    teaspoon = teaspoon - teaPerCup * cup
    tablespoon = teaspoon // teaPerTab
    teaspoon = teaspoon - teaPerTab * tablespoon
    if cup > 0:
        result = result + str(cup) + ' cup'
        if cup > 1:
            result += 's'
    if tablespoon > 0:
        if result != '':
            result += ', '
        result = result + str(tablespoon) + ' tablespoon'
        if tablespoon > 1:
            result += 's'
    if teaspoon > 0:
        if result != '':
            result += ', '
        result = result + str(teaspoon) + ' teaspoon'
        if teaspoon > 1:
            result += 's'
    return result
def main():
    unitNumber = eval(input('Please enter the number of unit: '))
    measureUnit = input('Please enter the unit of measure: ')
    print(volume(unitNumber, measureUnit))
main()