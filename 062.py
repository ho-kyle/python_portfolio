a = [4.95, 9.95, 14.95, 19.95, 24.95]
for i in range(5):
    originalPrice = a[i]
    discountAmount = a[i] * 0.6
    newPrice = a[i] * 0.4
    print(f'the original price: {originalPrice:5.2f}, the discount amount: \
{discountAmount:5.2f}, the new price: {newPrice:5.2f}')