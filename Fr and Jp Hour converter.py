#Thank you for using this converter!
#Made by Amaryne B. (a.k.a. TasDeNeige), 01/10/2022

print("\n/!\ Warning: This converter uses the 24h format /!\ ") #I hate 12h format >:(

while True == True: #Repeats the program so you don't have to do it yourself ;)

    mode = 0    
    while mode != 1 and mode != 2 and mode != 3 : #Forces the user to chose a valid mode
        mode = int(input("What do you want to convert? \nFr to Jp (1) | Jp to Fr (2) | End (3) -> "))

    #------------------ FR TO JP ------------------#
    if mode == 1:
        print("--------------------")
        FrHour = int(input("French hour to convert -> "))
        print(str(FrHour) + "h in France")

        JpHour = FrHour + 7

        if JpHour >= 24: #Corrects the hour
            JpHour -= 24

        print(str(JpHour) + "h in Japan")
        print("--------------------")
    
    #------------------ JP TO FR ------------------#
    elif mode == 2:
        print("--------------------")
        JpHour = int(input("Japanese hour to convert -> "))
        print(str(JpHour) + "h in Japan")

        FrHour = JpHour - 7

        if FrHour < 0: #Corrects the hour
            FrHour = 17 + JpHour #"17" is because 24 - 7 = 17

        print(str(FrHour) + "h in France")
        print("--------------------")

    #------------------ END ------------------#
    else:
        print("See you soon!") # :D
        break