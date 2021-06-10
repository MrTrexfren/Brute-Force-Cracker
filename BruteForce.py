import pyautogui
import os
import random
import time

password = pyautogui.password("Enter a Password:")
pass_len = len(password)
password_con = []
rand_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
              'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
crack = False

if pass_len >= 20:
    print("Sorry your password is to long try again.")
    time.sleep(2)
    os.system("exit")

else:
    print("Remember: The longer the password is the longer it will take to crack.")
    print("Brute Force password cracking is a long process so be patient.")

for i in range(pass_len):
    password_con.append(" ")

while not crack:
    for i in range(pass_len):
        password_con[i] = random.choice(rand_chars)
        print("Char ", i + 1, password_con[i])

    time.sleep(0.1)
    os.system("cls")

        if char_type == 1:
            pass_guess[i] = rand_lower
        elif char_type == 2:
            pass_guess[i] = rand_upper
        elif char_type == 3:
            pass_guess[i] = rand_num

    time.sleep(0.1)
