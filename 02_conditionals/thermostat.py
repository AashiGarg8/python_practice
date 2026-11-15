device_status = input("Ur device status: ").lower()
temp = float(input("ur body temp: "))
if device_status == "active":
    if temp > 35:
        print("High temp")
    else:
        print("Normal temp")

else:
    print("Device offline")


