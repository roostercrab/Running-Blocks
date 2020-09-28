def set_level(score, SPEED):
  if score < 10:
    SPEED = 10
  elif score < 20:
    SPEED = 20
  elif score < 30:
    SPEED = 30
  else:
    SPEED = 40
  return SPEED