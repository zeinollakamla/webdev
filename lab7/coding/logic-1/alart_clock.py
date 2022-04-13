def alarm_clock(day, vacation):
  if day<6 and day>0 and not vacation:
    return "7:00"
  elif ((day==0 or day==6) and not vacation) or (day<6 and day>=1 and vacation):
    return "10:00"
  else:
    return "off"