import pandas
cities = pandas.read_csv("cities.csv")
# cities.head()
cities.to_html()

with open('weatherData.html', 'w') as fo:
    cities.to_html(fo)