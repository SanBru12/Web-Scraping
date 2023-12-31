import requests
from bs4 import BeautifulSoup


def get_url():
    return "https://www3.animeflv.net"


def get_TitlePage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string
    return title


def get_AnimeTitle(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    DivTitle = soup.select(".Title")
    ReturnTitles = []  # Aquí almacenaremos los títulos
    count = 0
    for div in DivTitle:
        count = count + 1
        if count > 2:
            title_text = div.get_text()
            ReturnTitles.append(title_text)
    return ReturnTitles


def get_AnimeImage(url, cant):
    count = 0
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    DivImage = soup.select(".Image")
    ReturnImage = []
    for img_tag in DivImage:
        img = img_tag.find("img")
        if img:
            image_src = img["src"]
            ReturnImage.append(url + image_src)
            count = count + 1
            if count == cant:
                break

    return ReturnImage


if __name__ == "__main__":
    url = get_url()
    img = get_AnimeImage(url)
    print(img)
