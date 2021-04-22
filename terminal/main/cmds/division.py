from files import vars

def division():
    if len(vars.history) == 0:
      vars.num_1 = float(input("Enter a number: "))
      vars.num_2 = float(input("Enter another number: ")) 
      vars.result = vars.num_1 / vars.num_2
      print(vars.result)
      vars.history.append(vars.result)
    else:
      vars.num = float(input("Enter a number again: "))
      vars.result = vars.history[len(vars.history) - 1] /  vars.num
      print(vars.result)
      vars.history.append(vars.result)
