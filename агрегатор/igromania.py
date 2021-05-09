#IGROMANIA
import bs4, requests

def igrm_names():
    print("10 последних новостей индустрии на IGROMANIA:\n")
    name_arr = []
    url = 'https://www.igromania.ru/news/game/'
    sep = '\"'
    j = 24

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    out = soup.find_all(class_='aubli_name')

    for item in out:
        name_arr.append(item.text)

    for i in range (1,14):
        del name_arr[j]
        j = j -1
    
    return(name_arr)

def igrm_links():
    link_arr = []
    url = 'https://www.igromania.ru/news/game/'
    sep = '\"'
    j = 24

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    out = soup.find_all(class_='aubli_name')

    for item in out:
        str1 = str(item)
        str1 = str1[28:]
        str1 = str1.split(sep, 1)[0]
        link_arr.append("https://www.igromania.ru/"+str1)

    for i in range (1,14):
        del link_arr[j]
        j = j -1
    
    return(link_arr)
def igrm_content():
    link_arr = igrm_links()
    arr = []
    arr1 = []
    j = 11
    for item in link_arr:
        url = item
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="page_news_content haveselect")
        for item in out:
            str1 = str(item.text)
            str1 = str1.replace("\r","")
            str1 = str1.replace("\n","")
            arr.append(str1)
    return arr

print(igrm_content())
