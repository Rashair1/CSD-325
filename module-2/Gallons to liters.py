#Rashai Robertson
#Cis245
#Week 4 Discussion
#This program converts gallons to liters

def intro ():
  print('This program converts gallons')
  print('to liters.')

  print('For your reference the formula is:')
  print('1 gallon = 3.78541 liters')

  print()
 
intro()

while True:
 def main():
  #display the intro screen
 
  
  try:
    #get the number of gallons
    gallons_needed = int(input('Enter the number of gallons: '))
    #convert the gallons to liters
    gallons_to_liters(gallons_needed)
  
  except:
    print("An exception occurred, try again by entering only a number")
    print()
    main()


 
 def gallons_to_liters(gallons):
  liters = gallons * 3.78541
  print('That converts to', liters, 'liters.')
  print()

 main()

