from files import vars
import math

def square_rt():
    vars.num = float(input("Enter a number: "))
    vars.result = math.sqrt(vars.num)
    print(vars.result)
    vars.history.append(vars.result)
