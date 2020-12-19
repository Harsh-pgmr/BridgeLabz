def wind_mill():
    try:
        while True
            temperature = int(input("Enter the Temperature from '0' to '50':"))
            if (temperature >= 0) and (temperature <= 50):
                print()
                windspeed = int(input("Enter the Wind Speed between '3' to '120' : "))
                if (windspeed >= 3) and (windspeed <= 120):
                    windchill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * pow(windspeed, 0.16);
                    print()
                    print("Temperature = ", temperature)
                    print("Wind speed  = ", windspeed)
                    print("Wind chill  = ", windchill)
                    print()
                else:
                    print("Enter the Valid Wind Speed");
            else:
                print("Enter the Valid Temperature")
                print()
    except ValueError:
        print("Please give the Valid input as Shown in the Statement above!!")
        print()
    except KeyboardInterrupt:
        print()
        print("Force Quit!!!!")
        print("Bye!!")


wind_mill()
