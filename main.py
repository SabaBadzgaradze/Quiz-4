import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

f = open("movies.csv", "w", encoding="utf-8-sig", newline="\n")
file = csv.writer(f)
file.writerow(["Title_GEO", "Title_ENG", "Year", "Image_URL"])
h = {"Accept-Language": "en-US"}

ind = 1

while ind <= 5:
    url = f"https://geo.saitebi.ge/main/new/{ind}"
    r = requests.get(url, headers=h)

    soup = BeautifulSoup(r.text, "html.parser")
    movie_content = soup.find("div", {"id": "content"})
    movie_list = movie_content.find_all("div", {"class": "movie-items-wraper"})

    for movie in movie_list:
        title_geo = movie.find("h4", {"class": "a"}).text
        title_eng = movie.find("h4", {"class": "b"}).text
        year = movie.find("span", {"class": "c"}).text
        base_url = "https://geo.saitebi.ge"
        image_url = base_url + movie.img.attrs["src"].replace(" ", "%")
        file.writerow([title_geo, title_eng, year, image_url])

    ind += 1
    sleep(10)