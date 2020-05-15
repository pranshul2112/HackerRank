year = int(input().strip())
if year >= 1919:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("12.09.",year, sep='')
    else:
        print("13.09.", year, sep='')
elif year == 1918:
    print("26.09.1918")
else:
    if (year % 4 == 0):
        print("12.09.", year, sep='')
    else:
        print("13.09.", year, sep='')
