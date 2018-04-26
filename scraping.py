import re, urllib.request

arrayofStocks = ["FB", "GOOG", "DATA", "BABA"]

url = "https://www.google.com/finance?q="

stock = input("Enter your stock: ")

url = url + stock
print(url)
url = "https://www.google.com/search?q=BHP"
data = urllib.request.urlopen(url).read()

#print(data)
'''
data1 = data.decode("utf-8")
m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
m = re.search("/", newString1)
'''