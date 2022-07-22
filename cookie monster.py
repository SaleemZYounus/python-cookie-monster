
def cookim(): 
  food_choice = input("What would u like to feed Cookie Monster")
  food_choice = food_choice.lower()

  print(food_choice)
  if food_choice == "cookie":
    print("Cookie Monster Happyyyyy")
    #print("sheeeeesh more than cookie")
  else:
    print("chill")
    cookim()
cookim()

