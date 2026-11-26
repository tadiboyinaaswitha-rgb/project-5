# PROJECT 5 – SMART PARKING FEE MANAGEMENT

## About the Project
The Smart Parking Fee Management project is designed to calculate parking charges based on vehicle category, 24-hour entry and exit timings, overnight stays, daily maximum caps, and lost-ticket penalties. It validates hour inputs and generates a clear itemized parking receipt.

## Technologies Used
- **Python** – Used to develop the smart parking fee calculator.
- **Conditional Statements** – Used to validate hours, detect overnight stays, and apply caps or penalties.
- **Arithmetic Operators** – Used to calculate parking duration, base charges, and total fees.
- **String Methods** – Used to normalize vehicle numbers, vehicle types, and lost-ticket choices.

## Main Features
- Accepts vehicle number, vehicle category (`BIKE`, `CAR`, `SUV`), entry/exit hours (`0–23`), and lost-ticket status.
- Validates that entry and exit hours fall within `0` to `23`.
- Detects overnight stays (`exit_hr < entry_hr`), adds 24 hours to duration, and charges a Rs. 100 overnight fee.
- Applies hourly rates with daily maximum caps and adds a Rs. 200 penalty if the ticket is lost.

## Algorithm
1. Start the program.
2. Read vehicle number, vehicle type, entry hour, exit hour, and lost-ticket status.
3. Verify that entry and exit hours are between `0` and `23`.
4. Compute parking duration and set the overnight flag if `exit_hr < entry_hr` (minimum 1 hour if equal).
5. Select the hourly rate and daily cap based on vehicle type.
6. Calculate capped base charge, add Rs. 100 if overnight, and add Rs. 200 if ticket is lost.
7. Display the smart parking receipt.
8. Stop the program.

## Sample Output
Enter vehicle number: AP39CD4521
Enter vehicle type (BIKE / CAR / SUV): CAR
Enter entry hour (0-23): 21
Enter exit hour (0-23): 5
Is parking ticket lost? (YES / NO): NO

----- SMART PARKING RECEIPT -----
Vehicle Number   : AP39CD4521
Category         : CAR
Duration         : 8 hour(s)
Parking Charge   : Rs. 250
Overnight Charge : Rs. 100
Lost Penalty     : Rs. 0
---------------------------------
Total Fee Payable: Rs. 350

## Conclusion
This project handles parking duration rules, rate caps, and penalty charges accurately. It demonstrates Python concepts such as conditional statements, arithmetic operators, and string methods.
