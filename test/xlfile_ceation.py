from openpyxl import Workbook

wb = Workbook()
ws = wb.active
datasheet = [["username", "password"],["bhanuone@gmail.com","12341"], ["bhanutwo@gmail.com","12342"], ["bhanuthree@gmail.com","12343"]]
for data in datasheet:
    ws.append(data)
wb.save("tut.xlsx")
