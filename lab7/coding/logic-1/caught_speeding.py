def caught_speeding(speed, is_birthday):
  if (speed <=60 and not is_birthday) or (speed <=65 and is_birthday):
    return 0
  elif (speed>=61 and speed<=80 and not is_birthday) or (speed>=61 and speed<=85 and is_birthday):
    return 1
  else:
    return 2