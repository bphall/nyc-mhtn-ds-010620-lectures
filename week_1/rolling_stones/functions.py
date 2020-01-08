# Find by name - Takes in a string that represents the name of an album. Should return a dictionary with the correct album, or return None.
def find_by_name(name):
    for item in rolling_final:
        if item['album'] == name:
            return item
   

# Find by rank - Takes in a number that represents the rank in the list of top albums and returns the album with that rank. If there is no album with that rank, it returns None.
def find_by_rank(num):
    for item in rolling_final:
        if item['number'] == str(num):
            return item
    print('None')

        
# Find by year - Takes in a number for the year in which an album was released and returns a list of albums that were released in that year. If there are no albums released in the given year, it returns an empty list.
def find_by_years(num1, num2):
    albums_released = []
    for item in rolling_final:
        if int(item['year']) in range(num1, num2+1):
            albums_released.append(item)
    return albums_released


# Find by ranks - Takes in a start rank and end rank. Returns a list of albums that are ranked between the start and end ranks. If no albums are found for those ranks, then an empty list is returned.
def find_by_ranks(num1, num2):
    albums_released = []
    for item in rolling_final:
        if int(item['number']) in range(num1, num2+1):
            albums_released.append(item)
    return albums_released


# All titles - Returns a list of titles for each album.
def titles():
    titles = []
    for item in rolling_final:
        item['album'].append(titles)
    return titles


# All artists - Returns a list of artist names for each album.
def artists():
    names = []
    for item in rolling_final:
        names.append(item['artist'])
    return names

# Artists with the most albums - Returns the artist with the highest amount of albums on the list of top albums
def most_albums():
    mydict = {}
    currentmaxval = 0
    currentmax = {}
    for item in allarts:
        mydict[item] = allarts.count(item)
    for k,v in mydict.items():
        if v > currentmaxval:
            currentmaxval = v
            currentmax = {k,v}
    return currentmax


# Most popular word - Returns the word used most in amongst all album titles
def most_pop_word():
    alltitles = titles()
    mydict = {}
    words = []
    currentmaxval = 0
    currentmax = {}
    for item in alltitles:
        words.extend(item.split(' '))
    for word in words:
        mydict[word] = words.count(word)
    for word, number in mydict.items():
        if number > currentmaxval:
            currentmaxval = number
            currentmax = {word, number}
    return currentmax




# Histogram of albums by decade - Returns a histogram with each decade pointing to the number of albums released during that decade.
year_list = []
years_int = []
for item in rolling_final:
    year_list.append(item['year'])
for year in year_list:
    years_int.append(int(year))
years_hist = []
for year in years_int:
    if year in range(1950,1960):
        years_hist.append(1960)
    if year in range(1960,1970):
        years_hist.append(1970)
    if year in range(1970,1980):
        years_hist.append(1980)
    if year in range(1980,1990):
        years_hist.append(1990)
    if year in range(1990,2000): 
        years_hist.append(2000)
    if year in range(2000,2010): 
        years_hist.append(2010)
    if year in range(2010,2020): 
        years_hist.append(2020)
    
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.hist(years_hist, bins=7, edgecolor='black')
plt.ylabel('No of times')
plt.xlabel('Decade')
plt.show()


# Histogram by genre - Returns a histogram with each genre pointing to the number of albums that are categorized as being in that genre.
year_list = []
years_int = []
for item in rolling_final:
    year_list.append(item['year'])
for year in year_list:
    years_int.append(int(year))
genre_hist = []
for year in years_int:
    if year in range(1950,1960):
        genre_hist.append(1950)
    if year in range(1960,1970):
        genre_hist.append(1960)
    if year in range(1970,1980):
        genre_hist.append(1970)
    if year in range(1980,1990):
        genre_hist.append(1980)
    if year in range(1990,2000): 
        genre_hist.append(1990)
    if year in range(2000,2010): 
        genre_hist.append(2000)
    
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.hist(genre_hist, bins=5, edgecolor='black')
plt.ylabel('No of times')
plt.xlabel('Decade')
plt.show()






        









