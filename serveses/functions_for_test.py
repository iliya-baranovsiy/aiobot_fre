from random import randint


def first(digit):
    if digit == "1":
        balls = 5
    elif digit == "2":
        balls = 10
    elif digit == "3":
        balls = 15
    return balls


def second(digit):
    if digit == "1":
        balls = 15
    elif digit == "2":
        balls = 5
    elif digit == "3":
        balls = 10
    return balls


def third(digit):
    if digit == "1":
        balls = 5
    elif digit == "2":
        balls = 15
    elif digit == "3":
        balls = 10
    return balls


def four(digit):
    if digit == "1":
        balls = 5
    elif digit == "2":
        balls = 10
    elif digit == "3":
        balls = 15
    return balls


def five(digit):
    if digit == "1":
        balls = 5
    elif digit == "2":
        balls = 10
    elif digit == "3":
        balls = 15
    return balls


def six(digit):
    if digit == "1":
        balls = 10
    elif digit == "2":
        balls = 15
    elif digit == "3":
        balls = 5
    return balls


def count(arr):
    count = 0
    res = 0
    image = ""
    arr_n = []
    for i in arr:
        count += i
    if count <= 35:
        res = randint(10, 25)
        image = "datas/roffles/111.jpg"
        arr_n.append(res)
        arr_n.append(image)
    elif (count <= 65) and (count > 35):
        res = randint(26, 53)
        image = "datas/roffles/123.jpg"
        arr_n.append(res)
        arr_n.append(image)
    elif (count <= 90) and (count > 65):
        res = randint(54, 88)
        image = "datas/roffles/photo_5454352567929791008_y.jpg"
        arr_n.append(res)
        arr_n.append(image)
    elif count >= 91:
        res = randint(88, 120)
        image = "datas/roffles/66.jpg"
        arr_n.append(res)
        arr_n.append(image)
    return arr_n
