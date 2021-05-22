def fare(dist):
    base_fare = 4.00
    every_X_meters = 140
    every_140_meters_fare = 0.25
    a = dist % 140
    if a != 0:
        dist //= every_X_meters
        cost = base_fare + (dist + 1) * every_140_meters_fare
        return cost
    else:
        dist /= every_X_meters
        cost = base_fare + dist * every_140_meters_fare
        return cost
dist = eval(input('Please enter the distance traveled (in kilometers): '))
print(f'The total fare: {fare(dist):.2f}')