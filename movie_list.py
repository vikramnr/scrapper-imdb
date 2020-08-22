import urllib3
import sys
from tqdm import tqdm
from bs4 import BeautifulSoup

year = str(sys.argv[1])
if(int(year)<1990 and int(year)>2019):
    print('Please enter valid year between 1990-2019')
else:
    url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"
    outUrl = urllib3.PoolManager().request('GET',url).data
    soup = BeautifulSoup(outUrl, 'lxml')
    movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
    i=1
    for div_item in tqdm(movieList):
        div = div_item.find('div',attrs={'class':'lister-item-content'})
        header = div.findChildren('h3',attrs={'class':'lister-item-header'})
        print('Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
        i += 1
