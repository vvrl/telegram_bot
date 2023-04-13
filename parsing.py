import requests
from bs4 import BeautifulSoup
import lxml



def parsing_weather():
    url = 'https://pogoda.mail.ru/prognoz/moskva/'
    response = requests.get(url)
    #print(response.text)


    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    tb = soup.find('div', class_= 'information__content__temperature')
    #print(tb.text)
    return tb.text

    # soup = bs(response.text, "html.parser")
    # vacancies_names = soup.find_all('span', class_='information__content__temperature')
    # for name in vacancies_names:
    #     print(name.a['title'])


    # bs = BeautifulSoup(response.text, "lxml")
    # #print(bs)

    # temp = bs.find('<td width="40%" style="border-bottom: 1px solid #D3D3D3;" align="center">')
    # print(temp)

