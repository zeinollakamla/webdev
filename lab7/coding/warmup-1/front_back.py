def front_back(str):
  if len(str)<=1:
    return str
  
  main = str[1:len(str)-1]
  
  return str[-1] + main + str[0]
