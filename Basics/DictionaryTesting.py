kwargs = {'arg': 'Bob', 'app': 'Niko'}
for i in kwargs.values():
    if i == 'Bob':
        print('Chungus')
    else:
        print('None')


monthConversions = {

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "M": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

    # Також можна в ключах юзати цифри (0, 2...) замість букв або слів ( 13: "Chung" )

    0: "Chung"

}

print(monthConversions["Dec"])
print(monthConversions.get("Jul"))
print(monthConversions.get("Rub", "Not a valid key"))
print(monthConversions[0])


