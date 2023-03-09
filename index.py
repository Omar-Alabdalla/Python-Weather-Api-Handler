import Weather

weatherList = []
using = True

while True:
    userIn = str(input(
        "\nInput (1) if you want to search a new zipcode, or (2) if you want to search all the zipcodes you've searched already. "))
    if userIn == "1":
        userInput = str(input("\nInput a zipcode to search: "))
        userinp = str(input(
            "\nInput (1) for the temperature, (2) for information on the wind, or (3) for basic locational information. "))
        if userinp == "1":
            print(Weather.getTemp(userInput))
        elif userinp == "2":
            print(Weather.getWind(userInput))
        elif userinp == "3":
            print(Weather.getLoc(userInput))
        weatherList.append(userInput)
    elif userIn == "2":
        userinp = str(input(
            "\nInput (1) for the temperature, (2) for information on the wind, or (3) for basic locational information. "))
        us = str(input(
            "Please input (1) if you want your results to be outputted normally, or (2) for them to be backwards."))
        if us == "1":
            if weatherList:
                for i in weatherList:
                    if userinp == "1":
                        print(Weather.getTemp(i))
                    elif userinp == "2":
                        print(Weather.getWind(i))
                    elif userinp == "3":
                        print(Weather.getLoc(i))
            else:
                print("\nPlease input a zipcode prior to using this function. ")
        elif us == "2":
            if weatherList:
                for i in weatherList:
                    if userinp == "1":
                        print(Weather.getTemp(i)[::-1])
                    elif userinp == "2":
                        print(Weather.getWind(i)[::-1])
                    elif userinp == "3":
                        print(Weather.getLoc(i)[::-1])
            else:
                print(
                    "\nPlease input a zipcode prior to using this function. "[::-1])
        else:
            print("\ninvalid output")

    else:
        print("\nYou have inputted an invalid variable")
        break
