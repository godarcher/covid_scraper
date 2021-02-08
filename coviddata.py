
#! This program fetches live covid information from the covid api.

# covid dependency
from covid import Covid

#?###########
#* Settings #
#?###########

show_countries = True

# We initialize covid
covid = Covid()

# Printing global data
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())

if show_countries == True:
    countries = covid.list_countries()
    for x in countries:
        print(x)

# get specific country related covid stats
cases_nl = covid.get_status_by_country_name("Netherlands")
cases_eng = covid.
United Kingdom

# printing country's data using for loop
for x in cases:
    print(x, ":", cases[x])
