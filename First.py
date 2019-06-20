
##inc the cmd after changing path use : python -m pip install [packagename]
##in this case- packagename is bs4
##python -m pip install requests beautifulsoup4 pandas

import pandas as pd
import requests
import bs4



from bs4 import BeautifulSoup as soup

# r = requests.get("https://www.ynet.co.il/articles/0,7340,L-5512967,00.html")
r = requests.get("https://www.ynet.co.il/articles/0,7340,L-5513037,00.html")

c = r.content
c

soup = soup(c, "html.parser")
# print(soup.prettify())

listings = []
#Extracting the headers:

all = soup.find("div", {"class":"art_header_title"}).text
all
all_sub = soup.find("div", {"class": "art_header_sub_title"}).text
all_sub

listings = all+ '\n' + all_sub
print(listings)


#Extracting the hyperlinks text:

hyper = soup.find_all("a", {"class":"bluelink"})
for h in hyper:
    print(h.text)

#Extracting the hyperlinks URL:

url = soup.find_all("a", {"class":"bluelink"})
for u in url:
    print(u.get('href'))

#Combining them both into a dictionary:

dict = {}
for d in soup.find_all("a", {"class":"bluelink"}):
    dict[d.text] = d.get('href')
print("The date of publishing is : ", soup.find_all("span", {"class":"art_header_footer_author"})[1].text)
print(dict)

all_headers =[]
all_headers.append(listings)
all_headers.append(dict)
print(all_headers)

#Exporting the data as a dataframe
df_headers = pd.DataFrame(all_headers)
print(df_headers)
df_headers.to_csv("All_headers.csv", index=False)

#Making a list of all ynet headlines:

r = requests.get("https://www.ynet.co.il")

c = r.content
c

soup = soup(c, "html.parser")

main_header = "The main headline is: " +  soup.find("span", {"class":"subtitle"}).text
main_link = "Link: "+ "https://www.ynet.co.il"+ soup.find("a", {"class":"sub-title"}).get("href")
print(main_header ,"\n", main_link)
# print("Link: "+ "https://www.ynet.co.il"+ soup.find("a", {"class":"sub-title"}).get("href"))
dict = {}
for d in soup.find_all("div", {"class":"title"}):
    dict[d.text] = d.get('href')
# print("The date of publishing is : ", soup.find_all("span", {"class":"art_header_footer_author"})[1].text)
print("The sub-titles are: \n", dict)

mini = soup.find_all("div", {"class":"cell cwide layout1"})
type(mini)
print(mini)

for m in mini:
    print(m.find_all("a", href= True))
    for h in m:
        print(h.find("div", {"class":"title"}).text)
        # print("https://www.ynet.co.il"+h.get("href"))






# test = '''<a href="/articles/0,7340,L-5514399,00.html"><div class="str3s_txt"> </div></a> '''
# print(soup(test).find("a", href = True).get("href"))