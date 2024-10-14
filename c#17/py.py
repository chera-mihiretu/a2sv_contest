def calc(candy, mid):
        a, b = 0, 0
        turn = True
        while candy:
            print("A :",  a,"B : ",  b)
            if turn:
                a += mid 
                candy = max(0, candy - mid)
                turn = False
            else:
                b += candy // 10
                candy -= candy // 10
                turn = True
        return a >= b

calc(41, 1)