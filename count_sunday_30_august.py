start = int(input("Enter the starting year: "))
end = int(input("Enter the ending year: "))

total_yrs = end - start
print("total yrs:", total_yrs)

leap_yrs = total_yrs // 4
print("Leap yrs", leap_yrs)

no_of_days = (total_yrs * 365) - leap_yrs
print("Days", no_of_days)

count_sundays = no_of_days // 7
print(count_sundays)