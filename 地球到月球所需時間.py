dist = 384400
speed_per_hour = 1225
total_hours = dist // speed_per_hour
days, hours = divmod(total_hours, 24)
print('需要天數')
print(days)
print('小時')
print(hours)