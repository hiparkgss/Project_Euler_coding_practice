year_range = range(1900, 2000 + 1)
file = 'problem_19_date.txt'
with open(file) as f:
    date_list = [int(line.rstrip('\n')) for line in f.readlines()]

date_dic = dict(enumerate(date_list, start=1))

sunday_date = []
day = 7

for year in year_range:
    month = 1

    if year % 400 == 0:
        date_dic[2] = 29
        while month < 13:
            while day < date_dic[month]:
                sunday_date.append([year, month, day])
                day += 7
            day = day - date_dic[month]
            month += 1

    elif year % 100 == 0:
        date_dic[2] = 28
        while month < 13:
            while day < date_dic[month]:
                sunday_date.append([year, month, day])
                day += 7
            day = day - date_dic[month]
            month += 1


    elif year % 4 == 0:
        date_dic[2] = 29
        while month < 13:
            while day < date_dic[month]:
                sunday_date.append([year, month, day])
                day += 7
            day = day - date_dic[month]
            month += 1

    else:
        date_dic[2] = 28
        while month < 13:
            while day < date_dic[month]:
                sunday_date.append([year, month, day])
                day += 7
            day = day - date_dic[month]
            month += 1

first_sunday = [sunday_date[i] for i in range(len(sunday_date))
                if sunday_date[i][2] == 1 and sunday_date[i][0] > 1900]
print(len(first_sunday))
print(first_sunday)