filepath = "/Users/henryham/Desktop/Coding Projects/TimbyTips/timbytips.txt"
clipboard = "/Users/henryham/Desktop/Coding Projects/TimbyTips/clipboard.txt"

done  = False

while not done:
    date = input("date [MM/DD/YY] ")
    day = input("day of week ")
    amtMade = input("amount made ")
    ampm = input("am/pm ")
    while (ampm != "am") and (ampm != "pm"):
        ampm = input("am/pm ")
    rating = input("rate 1-10 ")
    input_list = [date,day,amtMade,ampm,rating]
    input_string = date + "," + day + "," + amtMade + "," + ampm + "," + rating + "\n"
    with open(filepath, "a") as file:
        file.write(input_string)
    yn = input("log another shift? y/n or DELETE? d\n")
    while yn != "y" and yn != "n" and yn != "d":
        yn = input("y/n/d")
    if yn == "n":
        done = True
    elif yn == "d":
        lines = []
        with open(filepath, 'r') as file:
            for line in file:
                if line != input_string:
                    lines.append(line)
        with open(filepath, 'w') as file:
            for line in lines:
                file.write(line)
        again = input("log another shift? y/n")
        if again != 'y':
            done = True
