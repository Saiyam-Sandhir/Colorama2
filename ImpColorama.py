"""
Copyright (c) Saiyam Jain 2021. All rights reserved.
Copyrights licensed under the Apache License 2.0.
See the accompanying LICENSE file for terms.
"""

#importing os module
import os

#defing check method that returns true if colorama package is getting imported and false if not
def check():
        
    #a loop that runs only twice
    #checks if colorama package is getting imported or not
    #if gets imported breaks with variable check = True
    #if not getting imported installs it and still if colorama package is getting imported breaks with variable check = False
    for i in range(2):
        
        #trying to import colorama package
        try:
            import colorama
            check = True
            break
        
        #if trial of importing colorama package is leading to error
        except:
            
            #if already tried to install colorama once
            if i == 1:
                break
            
            #running the pip install command in cmd to install the colorama package
            os.popen("pip install colorama")
            check = False
            
    return check


            






