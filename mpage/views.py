from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bs4 import BeautifulSoup
import requests

def index():
    STATISTIC = 'https://www.worldometers.info/coronavirus/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130'}
    page = requests.get(STATISTIC, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    convert = soup.findAll('tbody')
    convert = convert[0]
    convert = soup.findAll('tr')


    info = {}

    name = None
    g = 8
    while g != 228:
        line = convert[g]
        stat = line.findAll('td')
        if g == 107:
            name = 'Reunion'
        elif g == 188:
            name = 'Curacao'
        else:
            name = str(stat[1].text)
        if name == 'Ukraine':
            for i in range(2, 13):
                if i == 1 or i == 7 or i == 9 or i == 10 or i == 11:
                    continue

                temp = stat[i].text
                temp = temp.replace(' ', '')
                temp = temp.replace('N/A', '')
                temp = temp.replace(',', '')
                temp = temp.replace('+', '')
                if g == 8 and i == 11:
                    temp = stat[i].text
                    pp = temp.find('.')
                    temp = temp[0: pp]

                try:
                    temp = int(temp)
                except Exception:
                    pass


                if i == 2:
                    stat_2 = temp
                elif i == 3:
                    stat_3 = temp
                elif i == 4:
                    stat_4 = temp
                elif i == 5:
                    stat_5 = temp
                elif i == 6:
                    stat_6 = temp
                elif i == 8:
                    stat_8 = temp
                elif i == 12:
                    stat_12 = temp
        g += 1

    info = {
        'country': 'Ukraine',
        'total_cases': stat_2,
        'new_cases': stat_3,
        'total_deaths': stat_4,
        'new_deaths': stat_5,
        'total_recovered': stat_6,
        'active_cases': stat_8,
        'total_tests': stat_12, }


    return info
	

def page_ru(request):
	info = index()
	
	return render(request, 'mpage/index.html', context=info)


def page_ua(request):
	info = index()
	return render(request, 'mpage/index-ua.html', context=info)

def page_en(request):
	info = index()
	return render(request, 'mpage/index-en.html', context=info)
	
	return render(request, 'mpage/index.html', context=info)
	