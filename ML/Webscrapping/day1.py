import requests as re 
from bs4 import BeautifulSoup as be

#  step 1  : Making the get Request : 
x=re.get('https://www.geeksforgeeks.org/python-programming-language/')
# print(x)
# step 2  : Parsing the HTML  : 
s = be(x.content, 'html.parser')
# print(s.prettify())
# The information comes after this is still  not usefull we have to do something more   : 
# Now getting s title  : 
print(s.title)

# Getting the name of the tag
print(s.title.name)
 
# Getting the name of parent tag
print(s.title.parent.name)
# r = s.find('div', class_='entry-content')
# content = r.find_all('p')
# print(content)
 
# Finding by id
r = s.find('div', id= 'main')
 
# Getting the leftbar
leftbar = r.find('ul', class_='leftBarList')
 
# All the li under the above ul
lines = leftbar.find_all('li')
 
for line in lines:
    print(line.text)
# find all the anchor tags with "href"
for link in s.find_all('a'):
    print(link.get('href'))


images_list = []
 
images = s.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)