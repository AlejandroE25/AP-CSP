def monitor():

  phosphateLevel = .3

  current = get_posphate()
  mesg = "Posphates OK"
  
  if (current > phosphateLevel):
      mesg = "Posphates too high!"

  return mesg

# Functiion to simulate actual fish tank monitoring
def get_posphate():
  return .05