import matplotlib.pyplot as pt

pt.plot([1,-2,3,4],[6,9,10,-30])
pt.show()


def primes(num):
    val = 0
    while val < num / 2 :
        if num % 2 == 0:
            print("Not a prime")


weight = 60.0
for i in range(0,11):
    moonweight = weight / 6
    print(moonweight)
    weight = weight + 1

'''
import re
import urllib.request
arrayofStocks = ["FB", "GOOG", "DATA", "BABA"]
url = "https://www.google.com/finance?q="
stock = input("Enter your stock: ")
url = url + stock
data= urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print("The value of " + stock.upper() + " is " + final)

'''
import re
import urllib.request
#http://www.weather-forecast.com/locations/Paris/forecasts/latest
#city = input("Enter your city: ")
#print(city)
city = "Adelaide"
#######https://www.weather-forecast.com/locations/Adelaide/forecasts/latest
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
print(url)
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#m = re.search(city, data1)
m = re.search('section class="description">', data1)
print(m)
start = m.end()
end = start + 2400
newString = data1[start:end]
print(newString)
m = re.search("</span>", newString)
#print(m)
end = m.start() - 2
final = newString[0:end]
#print(final)