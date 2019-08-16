from bs4 import BeautifulSoup

html_sample =' \
<html> \
 <header> \
  <title> \
   This is title \
  </title> \
 </header> \
 <body> \
  Hello world \
 </body> \
</html>'

soup =BeautifulSoup(html_sample)
print(soup.prettify())   #html排版

print(soup.text)          
print(soup.contents)      #取全內容(list)
#print(soup.select("html")[0]) #取html標籤(全)內容(str)
print(soup.select("title"))  #取title標籤內內容(str)






