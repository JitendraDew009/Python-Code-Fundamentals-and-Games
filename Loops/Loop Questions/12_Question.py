# Build a train seat booking system 
seat_type = input("Enter seat type (Sleeper/AC/General/Luxury) here: ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds are available")
    case "ac":
        print("AC - Air Condtioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")
