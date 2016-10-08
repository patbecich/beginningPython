#program that converts numerical date to spelled out format

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month = raw_input('Give month (1-12)')
day = raw_input('Give day (1-31)')
year = raw_input('Give year')

month_number = int(month)
day_number = int(day)

endings = ['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] + 7*['th'] + ['st']






print "The date is: "+months[int(month)-1]+" "+ day+endings[day_number-1]+"," + year
