def myfunc(x, y):
    z = x * y
    print('the result is: ' + str(z))


myfunc(5, 4)
# lambda

vol = lambda h, w, l: h * w * l
print(vol(5, 6, 7))
