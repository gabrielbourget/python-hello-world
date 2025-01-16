import random

FEET_IN_A_MILE = 5280
METERS_IN_A_KM = 1000
beatles = ["John", "Paul", "George", "Ringo"]

def get_file_ext(filename):
  return filename[filename.index("."):]

def roll_dice(num):
  return random.randint(1, num)