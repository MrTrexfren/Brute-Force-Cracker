import random
import time
import pyautogui
import os

password = pyautogui.password("Enter a Password:")
password_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = ""

print("Remember the longer your password is the longer it will\ntake to crack.")

time.sleep(3)

conv_password = []

for i in range(len(password)):
    conv_password.append(" ")
    if password[i].isnumeric():
        for c in range(10):
            password_chars.append(str(c))


while password.lower() != result:
    for i in range(len(password)):
        result = "".join(conv_password)
        rand_char = random.choice(password_chars)
        conv_password[i] = rand_char
        print("<<<<", result, ">>>>")

    
    time.sleep(0.1)
    os.system("cls")


print("Done cracking your password is: ", result)
