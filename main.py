from models.bill import Bill
from models.flatmate import Flatmate
from models.pdf_report import PdfReport
from models.file_upload import UploadFile


print("\nThis programme generates pdf report of flatmates bill.")

# Get the bill details of a period
bill_amount = float(input("Enter the bill amount: "))
period = input("Enter the period(Ex: 2021 January): ")
curr_bill = Bill(bill_amount, period)

# Get the flatmates details
person_count = int(input("Enter number of flatmates staying in the flat: "))
flatmates = [0 for i in range(person_count)]
total_days = 0

print("Please enter the name and number of days stayed one by one")
for i in range(person_count):
    temp_name = (input("Enter the Name: ")).title()
    temp_no_of_days = int(input(f"Number of days stayed by {temp_name}: "))
    flatmates[i] = Flatmate(temp_name, temp_no_of_days)
    total_days += temp_no_of_days

pdf = PdfReport("Flatmate_bill.pdf")

pdf.generate_report(flatmates, curr_bill, total_days)

for i in flatmates:
    print(f"{i.name} has to pay {i.to_pay(curr_bill, total_days)} rupees.")

remote_file = UploadFile(file_path= pdf.name)
print(remote_file.upload())

