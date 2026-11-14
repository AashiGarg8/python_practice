#you are building a ticket info system for a railway app
#Based on seat type, show its features

#Task Input: "sleeper", "AC", "general", "Luxury"
# match using match-case
#Unknown -> show: "Invalid seat type"

# seat_type = input("Enter seat type(sleeper/AC/general/Luxury): ").lower()
# if(seat_type == "sleeper"):
#     print("It is a sleeper type")
# elif(seat_type == "AC"):
#     print("It is a AC seat")
# elif(seat_type == "general"):
#     print("It is a general type")
# elif(seat_type == "luxury"):
#     print("It is a luxury type")
# else:
#     print("Invalid Seat type")


seat_type = input("seat type(sleeper/ac/general/luxury):").lower()

match seat_type:
    case "general":
        print("geenral")
    case "sleeper":
        print("sleeper")
    case "ac":
        print("ac")
    case "aarav":
        print("hello aarav")
    case _:
        print("Invalid seat type")
