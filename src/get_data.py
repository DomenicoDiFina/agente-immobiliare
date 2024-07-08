from typing import List
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from models.apartment import Apartment


def get_data_from_immobiliare() -> List[Apartment]:
    url_all_apartments = get_all_apartments_from_immobiliare()
    apartment_list = []

    # print(url_all_apartments)

    for url_apartment in tqdm(url_all_apartments):
        response = requests.get(url_apartment)
        html_content = response.content

        soup = BeautifulSoup(html_content, "lxml")

        information_list = soup.find_all("dl", class_="re-realEstateFeatures__list")
        div_location = soup.find("div", class_="re-title__content")
        photos = soup.find_all("div", class_="nd-slideshow__item")

        photos_list = [photo.find("img")["src"] for photo in photos]

        try:
            comune = div_location.find_all("span", class_="re-title__location")[0].text
        except:
            comune = ""

        try:
            indirizzo = div_location.find_all("span", class_="re-title__location")[
                1
            ].text
        except:
            indirizzo = ""

        list_of_features = []

        for dl in information_list:
            informations = dl.find_all("dd")

            # Stampa gli elementi <dd>
            for information in informations:
                list_of_features.append(information.text)

        try:
            apartment = Apartment(
                list_of_features[0],
                list_of_features[1],
                list_of_features[2],
                list_of_features[3],
                list_of_features[4],
                list_of_features[5],
                list_of_features[6],
                list_of_features[7],
                list_of_features[8],
                photos_list,
                list_of_features[9],
                list_of_features[10],
                list_of_features[11],
                comune,
                indirizzo,
            )
            apartment_list.append(apartment)
        except:
            pass


def get_data_from_idealista() -> List[Apartment]:
    pass


def get_all_apartments_from_immobiliare() -> List[str]:
    apartment_list = []
    for page in range(1, 1000):
        url_immobiliare = f"https://www.immobiliare.it/affitto-case/milano-provincia/?criterio=rilevanza&prezzoMinimo=500&prezzoMassimo=750&superficieMinima=40&superficieMassima=80&localiMinimo=2&pag={page}"
        response = requests.get(url_immobiliare)
        html_content = response.content

        soup = BeautifulSoup(html_content, "lxml")

        all_apartments = soup.find_all("div", "in-listingCardPropertyContent")

        if all_apartments == []:
            break

        for apartment in all_apartments:
            link = apartment.find("a", href=True)
            href_aparment = str(link["href"])
            apartment_list.append(href_aparment)

    return apartment_list


if __name__ == "__main__":
    get_data_from_immobiliare()
