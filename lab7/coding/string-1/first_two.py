def first_two(str):
  if str == " ":
    return "yields the empty string"
  elif len(str) == 1:
    return str
  else:
    return str[:2]