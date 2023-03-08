#Class methods located here

# making the encoded password global - Jamison
stored_password = []


#This function brings up the menu
def menu():
  print('''Menu
---------------''')
  print('1. Encode\n2. Decode\n3. Quit\n')
  choice = int(input('Please enter an option: '))
  return choice

  
#This function gets the password from the user and stores it.
def encoder():
  while True:
		global stored_password
    encoded_password = str(int(input('Please enter your password to encode: ')))
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
def decoder():
  global stored_password
  encoded_password = stored_password[0]
  decoded_password = ''
  for digit in encoded_password:
      decoded_digit = str((int(digit) - 3) % 10)
      decoded_password += decoded_digit
  print(f'The decoded password is {decoded_password}, and the original password is {encoded_password}')
  print()


if __name__ == "__main__":
  while True:
    #User selects an option from the menu.
    choice = menu()

    #Encode Option
    if choice == 1:
      your_password = encoder()
      #print(f'Your password is {your_password}') ---> tests if inputed password was actually stored.

    #Decode Option
    elif choice ==  2:
      decoder()
      print()

    #Quit Option
    elif choice == 3:
      break

    #Invalid Choice Option
    else: 
      print('Invalid Choice. Please Select Again.')
      print()
      continue
