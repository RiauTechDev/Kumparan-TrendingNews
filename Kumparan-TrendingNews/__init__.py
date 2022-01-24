import requests
from bs4 import BeautifulSoup


# Extract data from Website

def data_extraction():
    try:
        content = requests.get('https://kumparan.com/trending',
                               headers={'Cache-Control': 'private, max-age=0, no-cache'})
    except Exception:
        return print('Fail Requests')

    if content.status_code == 200:
        # Get and assign TrendingNews Title, AuthorName, TimePublished
        soup = BeautifulSoup(content.text, 'html.parser')
        main = soup.find('div', {'class': 'Viewweb__StyledView-sc-1ajfkkc-0 cFmAia'})
        title = main.findChildren('span', {
            'class': 'Textweb__StyledText-sc-1uxddwr-0 eSSwLt CardContentweb__CustomText-sc-1gsg7ct-0 grhZrk'})
        author = main.findChildren('span', {
            'class': 'Textweb__StyledText-sc-1uxddwr-0 gACKQ CardContentweb__NameText-sc-1gsg7ct-1 '
                     'CardContentweb___StyledNameText-sc-1gsg7ct-2 bxUak erbwXr'})
        time = main.findChildren('span', {'class': 'Textweb__StyledText-sc-1uxddwr-0 bQqliI'})
        time = time[2::3]

        i = 0
        newsnumber = dict()
        titlename = dict()
        authorname = dict()
        timepublished = dict()

        for ti, thor, tim in zip(title, author, time):
            num = i + 1
            newsnumber[f'news{num}'] = num
            titlename[f'title{num}'] = ti.text
            authorname[f'author{num}'] = thor.text
            timepublished[f'time{num}'] = tim.text
            print(f"Trending News {newsnumber[f'news{num}']}: {titlename[f'title{num}']}, Author Name: {authorname[f'author{num}']}, Time Published: {timepublished[f'time{num}']}")
            i = i + 1


if __name__ == '__main__':
    data_extraction()