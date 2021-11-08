import csv
import requests
from bs4 import BeautifulSoup
import csv
html_text=requests.get('https://www.national.co.uk/tyres-search?width=205&profile=55&diameter=16').text
soup=BeautifulSoup(html_text,'html.parser')
details=soup.find_all('div',class_ ="col-md-6 tyreDisplay")
file=open('TyreData1.csv','w',newline="")
writer=csv.writer(file)
writer.writerow(['Name of Website','Tyre Brand','Tyre Pattern','Tyre Size','Seasonality','Price'])
for detail in details:
    brand=detail.find('img',loading='lazy')
    TyreBrand=brand['alt'].replace("\n",'')
    pattern=detail.find('a',class_="pattern_link")
    TyrePattern=pattern.text.replace("\n",'')
    sizes=detail.find('div',class_='details').find_all('p')
    TyreSize=sizes[1].text.replace("  ","").replace("\r","").replace('\n','')
    amount=detail.find('div',class_='price text-center padding-2').find_all('strong')
    Price=amount[0].text.replace("  ","").replace("\n",'').replace('\r','').replace('\xc2\xa3','')
    Seasonality=detail['data-tyre-season'].replace("\n",'')
    WebsiteName="www.national.co.uk"
    print(WebsiteName)
    print(TyreBrand)
    print(TyrePattern)
    print(TyreSize)    
    print(Price)
    print(Seasonality)
    writer.writerow([WebsiteName, TyreBrand, TyrePattern, TyreSize, Seasonality, Price])
file.close()