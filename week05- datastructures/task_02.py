
# 2. Create a tuple that stores the months of the year, from that tuple create
# another tuple with just the summer months (May, June, July), print out the
# summer months one at a time.

months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
summer_months = months_of_year[4:7]
for month in summer_months:
    print(month)