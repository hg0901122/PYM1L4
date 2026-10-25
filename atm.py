request = input("How much money would you like to withdraw?")
dinominition_100 = 100
request = int(request)
print("number of 100 notes needed:",request // dinominition_100)
reminder_1 = request % dinominition_100
print("number of 50 notes needed:",reminder_1 // 50)
reminder_2 = request % reminder_1
print("number of 20 notes needed:",reminder_2 // 20)