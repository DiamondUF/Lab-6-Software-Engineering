#Class methods located here

#This function brings up the menu
def menu():
  print('''Menu
---------------''')
  print('1. Encode\n2. Decode\n3. Quit\n')
  choice = int(input('Please enter an option: '))
  return choice

  
#This function gets the password from the user and stores it.
def encoder():
  stored_password = []
  while True:
    encoded_password= str(int(input('Please enter your password to encode: ')))
    #Asks user for a 8 digit password.
    if len(encoded_password) != 8: 
      print('Password must be 8-digits long.')
      print()
      continue
    #When the user puts in the password, it is stored.
    else:
      stored_password.append(encoded_password)
      print('Your password has been encoded and stored!')
      print()
      break
  return stored_password

  
#Was going to put the decoded function here
def decoder(your_password):
  pass


if __name__ == "__main__":
  while True:
    #User selects an option from the menu.
    choice = menu()

    #Encode Option
    if choice == 1:
      your_password = encoder()
      #print(f'Your password is {your_password}') ---> tests if inputed password was actually stored.
      print()

    #Decode Option
    elif choice ==  2:
      decoder(your_password)
      print()
      pass

    #Quit Option
    elif choice == 3:
      break

    #Invalid Choice Option
    else: 
      print('Invalid Choice. Please Select Again.')
      print()
      continue