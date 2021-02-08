
#! This program fetches live covid information from the covid api.

# covid dependency
from covid import Covid

# We initialize covid
covid = Covid()

# Printing global data
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())

# get specific country related covid stats
covid.list_countries()
#cases = covid.get_status_by_country_name("nl")

# printing country's data using for loop
for x in cases:
    print(x, ":", cases[x])
