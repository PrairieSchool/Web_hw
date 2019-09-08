import pandas
cities = pandas.read_csv("cities.csv")
cities.set_index("City_ID", inplace=True)
cities.to_html()

with open('weatherDataXXX.html', 'w') as fo:
    cities.to_html(fo)
    

cities.head()