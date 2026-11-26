vehicle_no = input("Enter vehicle number: ").upper()
v_type = input("Enter vehicle type (BIKE / CAR / SUV): ").upper()
entry_hr = int(input("Enter entry hour (0-23): "))
exit_hr = int(input("Enter exit hour (0-23): "))
lost = input("Is parking ticket lost? (YES / NO): ").upper()

if entry_hr < 0 or entry_hr > 23 or exit_hr < 0 or exit_hr > 23:
    print("Invalid time input. Hours must be between 0 and 23.")
else:
    overnight = False
    if exit_hr < entry_hr:
        duration = (24 - entry_hr) + exit_hr
        overnight = True
    elif exit_hr == entry_hr:
        duration = 1
    else:
        duration = exit_hr - entry_hr

    if v_type == "BIKE":
        rate, cap = 20, 120
    elif v_type == "SUV":
        rate, cap = 60, 350
    else:
        rate, cap = 40, 250

    base_fee = min(duration * rate, cap)
    overnight_fee = 100 if overnight else 0
    penalty = 200 if lost == "YES" else 0
    total_fee = base_fee + overnight_fee + penalty

    print("\n----- SMART PARKING RECEIPT -----")
    print("Vehicle Number   :", vehicle_no)
    print("Category         :", v_type)
    print(f"Duration         : {duration} hour(s)")
    print(f"Parking Charge   : Rs. {base_fee}")
    print(f"Overnight Charge : Rs. {overnight_fee}")
    print(f"Lost Penalty     : Rs. {penalty}")
    print("---------------------------------")
    print(f"Total Fee Payable: Rs. {total_fee}")
