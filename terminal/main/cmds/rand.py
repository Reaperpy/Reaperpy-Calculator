from files import vars
from cmds import add
from cmds import division
from cmds import expon
from cmds import subtract
from cmds import multiply
import random

def rand():
  if len(vars.history) == 0:
    vars.num_1 = random.randint(0, 100000)
    vars.num_2 = random.randint(0, 100000)
    vars.random_op = random.choice(vars.random_ops)
    if vars.random_op == "add":
      vars.result = vars.num_1 + vars.num_2
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "subtract":
      vars.result = vars.num_1 - vars.num_2
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "multiply":
      vars.result = vars.num_1 * vars.num_2
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "divide":
      vars.result = vars.num_1 / vars.num_2
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "expo":
      vars.result = vars.num_1 ** vars.num_2
      print(vars.result)
      vars.history.append(vars.result)
    else:
      pass

  else:
    vars.num = random.randint(0, 100000)
    vars.random_op = random.choice(vars.random_ops)
    if vars.random_op == "add":
      vars.result = vars.history[len(vars.history) - 1] + vars.num
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "subtract":
      vars.result = vars.history[len(vars.history) - 1] - vars.num
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "multiply":
      vars.result = vars.history[len(vars.history) - 1] * vars.num
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "divide":
      vars.result = vars.history[len(vars.history) - 1] / vars.num
      print(vars.result)
      vars.history.append(vars.result)
    elif vars.random_op == "expo":
      vars.result = vars.history[len(vars.history) - 1] ** vars.num
      print(vars.result)
      vars.history.append(vars.result)
    
