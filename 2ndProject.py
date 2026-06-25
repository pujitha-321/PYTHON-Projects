yourbirthYear = int(input("Enter your Birthday year: "))
yourbirthMonth = int(input("Enter your Birthday month: "))
yourbirthDay = int(input("Enter your Birthday Day: "))

current_year = 2026
current_month = 6
current_Day = 25

years = current_year - yourbirthYear
months = current_month - yourbirthMonth
days = current_Day - yourbirthDay

if days < 0:
    days = days +30
    months = months-1
if months<0:
    months = months +12
    years = years-1
  


print(f"my Age in years: {years}")
print(f"my Age in months:{months}")
print(f"my age in days:{days}")