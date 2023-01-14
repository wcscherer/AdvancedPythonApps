import main
## CLI IMPLEMENTATION

# Welcome banner
print("\n*** WELCOME TO THE ROOMMATE BILL CALCULATOR ***\n")

# Input the bill amount and period into the Bill instance
bill_period = input("Enter the bill period as MONTH YEAR (e.g. May 2022): ")

bill_amount = float(input("Enter the bill amount in dollars and cents (e.g. 1503.12): "))
bill_instance = main.Bill(amount=bill_amount, period=bill_period)
print("Billing period: {}; Bill amount: {:.2f}\n".format(bill_period, bill_amount))

# Input the user name and occupancy
user_name = str(input("Enter your full name (e.g. John Doe): "))
user_occupancy = int(input("Enter the number of days you, {}, resided in the apartment during the pay period: ".format(user_name)))
user = main.Roommate(name=user_name, days_in_unit=user_occupancy)

# Input the roommate's name and occupancy
roommate_name = str(input("Please enter your roommate's full name (e.g. Jane Doe): "))
roommate_occupancy = int(input("Enter the number of days your roommate, {}, resided in the apartment during the pay period: ".format(roommate_name)))
user_roommate = main.Roommate(name=roommate_name, days_in_unit=roommate_occupancy)

# Calculate the fraction of the bill to be paid and print the pdf
user_pays = user.pay_bill(bill_instance=bill_instance, other_roommate=user_roommate)
roommate_pays = user_roommate.pay_bill(bill_instance=bill_instance, other_roommate=user)
print("Roommate {} pays: {:.2f}".format(user.name, user_pays))
print("Roommate {} pays: {:.2f}".format(user_roommate.name, roommate_pays))

bill_report = main.PdfReport(file_name="Roommate-Bill-for-"+str(bill_instance.period).replace(" ","-")+'.pdf')
bill_report.generate_pdf(roommate1=user, roommate2=user_roommate, bill=bill_instance)