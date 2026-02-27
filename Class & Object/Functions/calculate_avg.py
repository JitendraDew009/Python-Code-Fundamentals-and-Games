#Avg of 3 Numbers

def calc_avg(a, b, c):
    sum = a + b + c # average = (a + b + c) / 3 
    avg = sum/3
    print(avg)
    return avg
calc_avg(1, 2, 3)

calc_avg(5, 15, 25)

# but if you use a + b + c / 3 then it is not correct experession to calc. avg. because /(division) has higher precedence 
# so it wtll act like a + b + (c/3).
# For example
# sum = 3 + 6 + 9 / 3
# sum = 3 + 6 + 3
# sum = 12