"""
Copyright (c) Saiyam Jain 2021. All rights reserved.
Copyrights licensed under the Apache License 2.0.
See the accompanying LICENSE file for terms.
"""

#importing sys module
import sys

#inserting the path of the package Colorama2 of SimpleDBMS in order to make use of modules in it
sys.path.insert(0, "G:\SimpleDBMS\Packages\Colorama2")

#importing ImpColoram module from the package Colorama2
import ImpColorama

#check method of ImpColorma module of Colorama2 package to check if colorama package is getting imported or not
check = ImpColorama.check()

#defining colPrint method that prints colored string given the color among the available and the string if colorama package is getting imported else just prints the string
def colPrint(color, string):
        
        #if ImpColorama module is functioning
        if check == True:
            
            #importing colorama package
            from colorama import Fore, Style
            
            #registered colors in the current version
            if color == "red": print(Fore.RED + string, Style.RESET_ALL)
            elif color == "blue": print(Fore.BLUE + string, Style.RESET_ALL)
            elif color == "green": print(Fore.GREEN + string, Style.RESET_ALL)
            elif color == "yellow": print(Fore.YELLOW + string, Style.RESET_ALL)
            else: print(string)
        
        #if ImpColorama module is not functioning
        else: print(string)

#there will be other decor methods and in the future version
