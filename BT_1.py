
import datetime

today = datetime.date.today()
date_str = input("Nhap ngay sinh (dd/mm/yyyy): ")
dateofbirth = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
age = today.year - dateofbirth.year
if (today.month, today.day) < (dateofbirth.month, dateofbirth.day):
    age -= 1
print(f"Tuoi cua ban la: {age}")