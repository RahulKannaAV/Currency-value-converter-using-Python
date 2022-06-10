import requests
from bs4 import BeautifulSoup


url = "https://fx-rate.net/USD/"
html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')

One_USD = {}

One_USD['EUR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Euro'}).text
One_USD['GBP'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Pound'}).text
One_USD['INR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Rupee'}).text
One_USD['CHF'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Franc'}).text
One_USD['CAD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Canadian Dollar'}).text
One_USD['AUD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Australian Dollar'}).text
One_USD['RMB'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Yuan'}).text
One_USD['RUB'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Ruble'}).text
One_USD['JPY'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Yen'}).text
One_USD['DZD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Dinar'}).text
One_USD['ARP'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Argentine Peso'}).text
One_USD['BRL'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Real'}).text
One_USD['BGN'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Lev'}).text
One_USD['CLP'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Chilean Peso'}).text
One_USD['HRK'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Kuna'}).text
One_USD['CZK'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Koruna'}).text
One_USD['DKK'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Danish Krone'}).text
One_USD['EGP'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Egyptian Pound'}).text
One_USD['ETH'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Ethereum'}).text
One_USD['HKD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Hong Kong Dollar'}).text
One_USD['HUF'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Forint'}).text
One_USD['ISK'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Krona'}).text
One_USD['IDR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Rupiah'}).text
One_USD['IRR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Rial'}).text
One_USD['ILS'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Shekel'}).text
One_USD['KRW'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Won'}).text
One_USD['MYR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Ringgit'}).text
One_USD['MXN'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Mexican Peso'}).text
One_USD['NZD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to New Zealand Dollar'}).text
One_USD['NGN'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Naira'}).text
One_USD['NOK'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Norwegian Krone'}).text
One_USD['PKR'] = soup.find('a',attrs={'class':'1rate','href':'/USD/PKR/','title':'Dollar to Rupee'}).text
One_USD['PHP'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Philippine Peso'}).text
One_USD['PLN'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Zloty'}).text
One_USD['QAR'] = soup.find('a',attrs={'class':'1rate','href':"/USD/QAR/",'title':'Dollar to Rial'}).text
One_USD['RON'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Leu'}).text
One_USD['SAR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Riyal'}).text
One_USD['RSD'] = soup.find('a',attrs={'class':'1rate','href':'/USD/RSD/','title':'Dollar to Dinar'}).text
One_USD['SGD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Singapore Dollar'}).text
One_USD['ZAR'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Rand'}).text
One_USD['LKR'] = soup.find('a',attrs={'class':'1rate','href':'/USD/LKR/','title':'Dollar to Rupee'}).text
One_USD['SEK'] = soup.find('a',attrs={'class':'1rate','href':'/USD/SEK/','title':'Dollar to Krona'}).text
One_USD['TWD'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Taiwan Dollar'}).text
One_USD['THB'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Baht'}).text
One_USD['TRY'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Lira'}).text
One_USD['UAH'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Hryvnia'}).text
One_USD['AED'] = soup.find('a',attrs={'class':'1rate','title':'Dollar to Dirham'}).text

