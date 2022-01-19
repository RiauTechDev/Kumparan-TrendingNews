import requests
import strip as strip
from bs4 import BeautifulSoup


# Extract data from Website

def data_extraction():
    try:
        content = requests.get('https://kumparan.com/trending')
    except Exception:
        return print('Fail Requests')

    if content.status_code == 200:

        #Get and assign TrendingNews Title, AuthorName, TimePublished
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'Viewweb__StyledView-sc-1ajfkkc-0 cFmAia'})
        result = result.findChildren('span', {'class': 'Textweb__StyledText-sc-1uxddwr-0 eSSwLt CardContentweb__CustomText-sc-1gsg7ct-0 grhZrk'})

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

        for res in result:
            if i == 0:
                news1 = res.text
            elif i == 1:
                news2 = res.text
            elif i == 2:
                news3 = res.text
            elif i == 3:
                news4 = res.text
            elif i == 4:
                news5 = res.text
            elif i == 5:
                news6 = res.text
            elif i == 6:
                news7 = res.text
            elif i == 7:
                news8 = res.text
            elif i == 8:
                news9 = res.text
            elif i == 9:
                news10 = res.text
            i = i + 1

        output = dict()
        output['news1'] = news1
        output['news2'] = news2
        output['news3'] = news3
        output['news4'] = news4
        output['news5'] = news5
        output['news6'] = news6
        output['news7'] = news7
        output['news8'] = news8
        output['news9'] = news9
        output['news10'] = news10

        return output
    else:
        return None


# Show data from extraction

def show_data(result):
    if result is None:
        print('Trending news is not found')
        return
    print('Trending News in Kumparan')
    print(f"Trending News 1 : {result['news1']}")
    print(f"Trending News 2 : {result['news2']}")
    print(f"Trending News 3 : {result['news3']}")
    print(f"Trending News 4 : {result['news4']}")
    print(f"Trending News 5 : {result['news5']}")
    print(f"Trending News 6 : {result['news6']}")
    print(f"Trending News 7 : {result['news7']}")
    print(f"Trending News 8 : {result['news8']}")
    print(f"Trending News 9 : {result['news9']}")
    print(f"Trending News 10 : {result['news10']}")

if __name__ == '__main__':
    result = data_extraction()
    show_data(result)










    # main = soup.find('div', {'class': 'Viewweb__StyledView-sc-1ajfkkc-0 dCdfue'})
    #
    # Title = soup.find('span', {
    #     'class': 'Textweb__StyledText-sc-1uxddwr-0 eSSwLt CardContentweb__CustomText-sc-1gsg7ct-0 grhZrk'})
    # AuthorName = soup.find('span', {
    #     'class': 'Textweb__StyledText-sc-1uxddwr-0 gACKQ CardContentweb__NameText-sc-1gsg7ct-1 CardContentweb___StyledNameText-sc-1gsg7ct-2 bxUak erbwXr'})
    # TimePublished = soup.find('div', {'class': 'Viewweb__StyledView-sc-1ajfkkc-0 eycOKo'})
    # TimePublished = TimePublished.findChildren('span', {'class': 'Textweb__StyledText-sc-1uxddwr-0 bQqliI'})











        # TitleRes = None
        # AuthorNameRes = None
        # TimePublishedRes = None
        #
        # TitleRes = Title.text
        # AuthorNameRes = AuthorName.text
        # TimePublishedRes = TimePublished[2].text
        # TimePublishedRes = TimePublishedRes.strip()
        # print(TitleRes + ', Author Name: ' + AuthorNameRes + ', Time Published: ' + TimePublishedRes)
        # print(result)

        # # Get and assign magnitude, depth, ls, bt, location, and perceived data
        # soup = BeautifulSoup(content.text, 'html.parser')
        # result = soup.find('div', {'class', 'Viewweb__StyledView-sc-1ajfkkc-0 dCdfue'})
        # result = result.findChildren('span', {'class' : 'Textweb__StyledText-sc-1uxddwr-0 bQqliI'})
        # print(result)