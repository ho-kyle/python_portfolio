def shippingCalculator(n):
    firstItem = 10.95
    subsequentItem = 2.95
    if n > 1:
        shippingCharge = firstItem + subsequentItem
        return(shippingCharge)
    elif n == 1:
        shippingCharge = firstItem
        return(shippingCharge)
    elif n == 0:
        shippingCharge = 0
        return(shippingCharge)
n = eval(input('Please enter the number of items \
purchased from you: '))
print(f'The shipping charge: {shippingCalculator(n):.2f}')
    