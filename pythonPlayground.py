# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below: 
def f_to_c(f):
  return (f - 32) * (5/9)

def c_to_f(c):
  return (c * (9/5)) + 32

def get_force(mass, acc):
  return mass * acc

def get_energy(mass):
  return c * mass

def get_work(mass, acc, distance):
  return get_force(mass, acc) * distance

train_force = get_force(train_mass, train_acceleration)

print(f" The GE train supplies {train_force} Newtons of force.")

print(f"A 1kg bomb supplies {get_energy(bomb_mass)} Joules")

print(get_work(train_mass, train_acceleration, train_distance))