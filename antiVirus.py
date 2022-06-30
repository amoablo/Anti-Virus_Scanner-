import os


infectedStart = False     #boolean that will be set to true if virus has been found
infectedend = False
path = input("Enter Path: ") #accept user input

route =  os.path.exists(path)#check if file path exist

if route:
    file = open(path,'r') #open file to read

    for line in file: #loop through each file of the file and check to see if the virus signature is there
        if('#qMeyivyOyh' in line):
            infectedStart=True
        if ('#XNjklgrVtg' in line):
            infectedend = True
    file.close() #close file

    #inform user if the file has been currupted or not
    if infectedStart and infectedend:
        print("File has been infected")
    else:
        print("File has not been infected")
else:
    print("ERROR: The path entered was incorrect") #Inform user that the file path is incorrect
