from cmds import add
from cmds import subtract
from files import vars
from cmds import multiply
from cmds import division
from cmds import expon
from cmds import rand
from cmds import squareroot
import random
import math

command = ""
separator = ", "

while True:
  try:
    command = input("> ")
    if command == "add":
      add.addition()
    elif command == "subtract":
      subtract.subtraction()
    elif command == "divide":
      division.division()
    elif command == "multiply":
      multiply.multiply()
    elif command == "expo":
      expon.exponents()
    elif command == "quit":
      break
    elif command == "view_history":
      print(vars.history)
    elif command == "clear_history":
      vars.history.clear()
      print("Calculator history cleared.")
    elif command == "random":
      rand.rand()
    elif command == "sqrt":
      squareroot.square_rt()
    else:
      print("I don't know that command.")
  except ValueError:
    print("Please enter an integer or float value.")
  except OverflowError:
    print("The result is too large to calculate!")
    rand.random()
