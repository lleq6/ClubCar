# Project CS436 By Baboon Team

import re
from tkinter import messagebox

class Checker:
    def usernameCheck(username : str):
        regex = "[A-Za-z0-9]+"
        if(re.fullmatch(regex, username)):
            return username
        else:
            messagebox.showwarning("Club Car", "Invalid username please try again!")
            return False
        
    def passwordCheck(password : str):
        if (len(password) >= 8 and len(password) <= 30): #and (not checkNum) and (not checkSpace) and not (checkAlpha):
            alp = 0
            num = 0
            spc = 0
            for char in password:
                if char.isalpha():
                    alp += 1
                elif char.isnumeric():
                    num += 1
                else:
                    spc +=1
            if alp >= 3 and num >= 3:
                return password
            else:
                messagebox.showwarning("Club Car", "Invalid password Please try again")
                return False
        else:
            messagebox.showwarning("Club Car", "Password can only have 8-30 character!\nPlease try again!")
            return False

    def emailCheck(email : str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            messagebox.showwarning("Club Car", "Invalid Email please try again!")
            return False
        
    def phoneCheck(phone : str):
        regex = "[0-9]+"
        if(re.fullmatch(regex, phone) and len(phone) == 10):
            return phone
        else:
            messagebox.showwarning("Club Car", "Invalid phone please try again!")
            return False