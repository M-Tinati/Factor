prices = [50, 120, 80, 300, 40, 200]

result = filter(lambda x : x > 100,prices)

print(list(result))


prices = [100, 200, 300, 400]

result1 = [x * 2 for x in prices if x > 100]
print(result1)