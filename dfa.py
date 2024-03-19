def stateZero (str):
  if str[0] == "1":
    return stateOne(str[1:len(str)])
  else:
    return stateZero(str[1:len(str)])

def stateOne(str):
  if str[0] == "1":
    return stateTwo(str[1:len(str)])
  else:
    return stateOne(str[1:len(str)])

def stateTwo(str):
  if str[0] == "1":
    return stateThree()
  else:
    return stateTwo(str[1:len(str)])

def stateThree():
    return True

print(stateZero("111"))