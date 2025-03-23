#Rashai Robertson
#CSD325
#Module 1.3
#3/21/2025


 #Making a function that counts down beer bottles to 1 before changing lyrics

def beer(bottles):
 
    #getting the range using a for loop to count backwards to 1. Iteration.

  for i in range(bottles, 0, -1):
      if i > 1:
          print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
      
      elif i == 1:
          print("1 bottle of beer on the wall, 1 bottle of beer.")
      
      print("Take one down and pass it around,")
      
      if i > 1:
          print(f"{i-1} bottle(s) of beer on the wall.")
      elif i == 1:
          print("0 bottles of beer on the wall.")
      print("\n")  # Adding a space

# Where the main program begins

#using input validation to print the program
try:
    bottles = int(input("How many bottles of beer are on the wall?: "))
    beer(bottles)
    print("Time to buy more beer bottles!")
except ValueError:
  print("Invalid input. Please enter a number.")
    


  
