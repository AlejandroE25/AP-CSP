def monitor():
  try:
    
    val1 = 28
    val2 = 35

    sal_levels = list(range(val1, val2))

    current = get_salinity()
    mesg = "Salinity OK"

    maxSalIndex = len(sal_levels) - 1

    if (current < sal_levels[0]):
      mesg = "Salinity too low!"
    elif (current > sal_levels[maxSalIndex]):
      mesg = "Salinity too high!"
    
  except:
    print("Unexpected error - Salinity Levels")

  return mesg

# Function to simulate actual fish tank monitoring
def get_salinity():
  return 31