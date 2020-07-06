from bs4 import BeautifulSoup
from decimal import Decimal

import re

def convert(amount, cur_from, cur_to, date, requests):
    params = { 'date_req' : date }
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params=params)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')
    if cur_from != 'RUR':
        From = Decimal(re.sub(r',', '.', str(soup.find('CharCode', text=cur_from).find_next_sibling('Value').text)))
        From_nom = Decimal(re.sub(r',', '.', str(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').text)))
    else:
        From = Decimal("1")
        From_nom = Decimal("1")
    if cur_to != 'RUR':
        To = Decimal(re.sub(r',', '.', str(soup.find('CharCode', text=cur_to).find_next_sibling('Value').text)))
        To_nom = Decimal(re.sub(r',', '.', str(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').text)))
    else:
        To = Decimal("1")
        To_nom = Decimal("1")

    result = (amount * From / From_nom) / (To / To_nom)
    return result.quantize(Decimal('0.0000'))  # не забыть про округление до 4х знаков после запятой
