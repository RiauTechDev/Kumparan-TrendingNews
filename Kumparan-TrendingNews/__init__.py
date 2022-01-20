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
        news1 = None
        news2 = None
        news3 = None
        news4 = None
        news5 = None
        news6 = None
        news7 = None
        news8 = None
        news9 = None
        news10 = None

        author1 = None
        author2 = None
        author3 = None
        author4 = None
        author5 = None
        author6 = None
        author7 = None
        author8 = None
        author9 = None
        author10 = None

        time1 = None
        time2 = None
        time3 = None
        time4 = None
        time5 = None
        time6 = None
        time7 = None
        time8 = None
        time9 = None
        time10 = None

        for ti, thor, tim in zip(title, author, time):
            if i == 0:
                news1 = ti.text
                author1 = thor.text
                time1 = tim.text
            elif i == 1:
                news2 = ti.text
                author2 = thor.text
                time2 = tim.text
            elif i == 2:
                news3 = ti.text
                author3 = thor.text
                time3 = tim.text
            elif i == 3:
                news4 = ti.text
                author4 = thor.text
                time4 = tim.text
            elif i == 4:
                news5 = ti.text
                author5 = thor.text
                time5 = tim.text
            elif i == 5:
                news6 = ti.text
                author6 = thor.text
                time6 = tim.text
            elif i == 6:
                news7 = ti.text
                author7 = thor.text
                time7 = tim.text
            elif i == 7:
                news8 = ti.text
                author8 = thor.text
                time8 = tim.text
            elif i == 8:
                news9 = ti.text
                author9 = thor.text
                time9 = tim.text
            elif i == 9:
                news10 = ti.text
                author10 = thor.text
                time10 = tim.text
            i = i + 1

        output = dict()
        output['news1'] = news1
        output['author1'] = author1
        output['time1'] = time1
        output['news2'] = news2
        output['author2'] = author2
        output['time2'] = time2
        output['news3'] = news3
        output['author3'] = author3
        output['time3'] = time3
        output['news4'] = news4
        output['author4'] = author4
        output['time4'] = time4
        output['news5'] = news5
        output['author5'] = author5
        output['time5'] = time5
        output['news6'] = news6
        output['author6'] = author6
        output['time6'] = time6
        output['news7'] = news7
        output['author7'] = author7
        output['time7'] = time7
        output['news8'] = news8
        output['author8'] = author8
        output['time8'] = time8
        output['news9'] = news9
        output['author9'] = author9
        output['time9'] = time9
        output['news10'] = news10
        output['author10'] = author10
        output['time10'] = time10

        return output
    else:
        return None


# Show data from extraction

def show_data(result):
    if result is None:
        print('Trending news is not found')
        return
    print('Trending News in Kumparan')
    print(f"Trending News 1: {result['news1']}, Author Name: {result['author1']}, Time Published: {result['time1']}")
    print(f"Trending News 2: {result['news2']}, Author Name: {result['author2']}, Time Published: {result['time2']}")
    print(f"Trending News 3: {result['news3']}, Author Name: {result['author3']}, Time Published: {result['time3']}")
    print(f"Trending News 4: {result['news4']}, Author Name: {result['author4']}, Time Published: {result['time4']}")
    print(f"Trending News 5: {result['news5']}, Author Name: {result['author5']}, Time Published: {result['time5']}")
    print(f"Trending News 6: {result['news6']}, Author Name: {result['author6']}, Time Published: {result['time6']}")
    print(f"Trending News 7: {result['news7']}, Author Name: {result['author7']}, Time Published: {result['time7']}")
    print(f"Trending News 8: {result['news8']}, Author Name: {result['author8']}, Time Published: {result['time8']}")
    print(f"Trending News 9: {result['news9']}, Author Name: {result['author9']}, Time Published: {result['time9']}")
    print(
        f"Trending News 10: {result['news10']}, Author Name: {result['author10']}, Time Published: {result['time10']}")


if __name__ == '__main__':
    result = data_extraction()
    show_data(result)
