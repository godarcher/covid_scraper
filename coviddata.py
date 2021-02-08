
#! This program fetches live covid information from the covid api.

# covid dependency
from covid import Covid

#?###########
#* Settings #
#?###########

show_countries = False

# We initialize covid
covid = Covid()

# Printing global data
print("")
print("Total confirmed cases in world:", covid.get_total_confirmed_cases())
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())
covid.get_total_confirmed_cases

if show_countries == True:
    countries = covid.list_countries()
    for x in countries:
        print(x)

# get specific country related covid stats
cases_nl = covid.get_status_by_country_name("Netherlands")
cases_eng = covid.get_status_by_country_name("United Kingdom")
cases_bel = covid.get_status_by_country_name("Belgium")
cases_ger = covid.get_status_by_country_name("Germany")
cases_france = covid.get_status_by_country_name("France")

# printing country's data using for loop
for x in cases_nl:
    print(x, ":", cases_nl[x])
