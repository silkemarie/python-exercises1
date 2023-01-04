def averager():
    sum = 0
    count = 0
    while True:
        value = yield
        if value is None:
            break
        sum += value
        count += 1
    return sum/count

average = averager()
next(average)
average.send(10)
average.send(20)
average.send(30)
result = average.send(None)
print(result)


