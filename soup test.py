import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.shopto.net/en/sony-wallet-topup/?currency=GBP').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# for para in soup.find_all('p'):
#     print(para.text)

print(soup.get_text())