available_size = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ").lower()) in available_size:
    print(f"Serving {requested_size} chai")

else:
    print(f"Size is unaviable - {requested_size}")