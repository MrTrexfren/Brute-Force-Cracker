import random
import pyautogui
import time

password = pyautogui.password("Enter Password")
pass_length = len(password)
pass_char = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
pass_guess = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
guessed_pass = ""

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'z']
numbers = ['1', '2', '3', '4',  '5', '6', '7', '8', '9']

for i in range(pass_length):
    pass_char[i] = password[i]
    pass_guess[i] = 0

if pass_length >= 20:
    password = guessed_pass
    print("Sorry you password is to long")
else:
    print("Remember the longer your password is the longer it will take to crack.\n")
    time.sleep(3)

while password != guessed_pass:
    print("========", "[",  pass_guess[0] ,  pass_guess[1],  pass_guess[2],  pass_guess[3],  pass_guess[4],  pass_guess[5], pass_guess[6],
           pass_guess[7],  pass_guess[8],  pass_guess[9],  pass_guess[10],  pass_guess[11],  pass_guess[12],  pass_guess[13],
          pass_guess[14],  pass_guess[15],  pass_guess[16],  pass_guess[17],  pass_guess[18],  pass_guess[19],  "]", "========")

    for i in range(pass_length):
        rand_lower = random.choice(lower_case)
        rand_upper = random.choice(upper_case)
        rand_num = random.choice(numbers)
        char_type = random.randint(1, 3)

        if char_type == 1:
            pass_guess[i] = rand_lower
        elif char_type == 2:
            pass_guess[i] = rand_upper
        elif char_type == 3:
            pass_guess[i] = rand_num

    time.sleep(0.1)
