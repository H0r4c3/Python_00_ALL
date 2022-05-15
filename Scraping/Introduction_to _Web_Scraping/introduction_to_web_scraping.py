'https://compucademy.net/introduction-to-web-scraping-with-python/'


import csv
import json
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup


def store_as_csv(data, headings=None):  # Don't use headings=[] as default argument. It behaves weirdly.
    if headings is None:
        headings = []

    with open(r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Introduction_to _Web_Scraping\data.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        # write title row
        writer.writerow(headings)

        # Write data
        for item in data:
            writer.writerow(item)


def store_as_json(data):
    # List to store dictionaries containing the data we extracted.
    records = []
    for item in data:
        new_record = {
            "title": item[0],
            "price": item[1]
        }
        records.append(new_record)
    # Write these to a JSON file.
    with open('data.json', 'w') as outfile:
        json.dump(records, outfile, indent=4)


if __name__ == "__main__":

    url = "http://books.toscrape.com/"

    try:
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        products = soup.find_all(class_="product_pod")
        data = []
        for product in products:
            title = product.find("h3").text
            price = float(product.find("div", class_="product_price").find("p", class_="price_color").text.strip("Â£"))
            data.append((title, price))
        store_as_csv(data, headings=["title", "price"])
        #store_as_json(data)
        print("### RESULTS ###")
        for item in data:
            print(*item)  # Don't let this phase you - it just unpacks the tuples for nicer display.
    except ConnectionError:
        print("Unable to open url.")