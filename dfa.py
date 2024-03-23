class DFA:
  def __init__(self, str):
    self.str = str
  def stateZero (self, str):
    if len(str) == 0:
      return False
    if str[0] == "1":
      return self.stateOne(str[1:len(str)])
    else:
      return self.stateZero(str[1:len(str)])

  def stateOne(self, str):
    if len(str) == 0:
      return False
    if str[0] == "1":
      return self.stateTwo(str[1:len(str)])
    else:
      return self.stateOne(str[1:len(str)])

  def stateTwo(self, str):
    if len(str) == 0:
      return False
    if str[0] == "1":
      return self.stateThree()
    else:
      return self.stateTwo(str[1:len(str)])

  def stateThree(self):
      return True
    
while True:    
  str = input("Enter a binary string: ")
  dfa = DFA(str)
  print(f"String is",  dfa.stateZero(str))