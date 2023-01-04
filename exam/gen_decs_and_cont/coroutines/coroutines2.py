def simple_coroutine():
    print("Started!")
    x = yield
    print("Received:", x)

coroutine = simple_coroutine()
print(coroutine)
coroutine.send(None)
coroutine.send(10)
