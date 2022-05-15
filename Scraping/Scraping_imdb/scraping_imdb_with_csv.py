'https://github.com/antoniablair/pyladies_scraping_workshop/blob/master/imdb_exercise_2_solution.md'


import csv, requests, time
from bs4 import BeautifulSoup


def get_film_stats(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    film = {}

    title = soup.h1.get_text()
    summary_text = soup.find('div', class_='summary_text').get_text()
    rating = soup.find('span', itemprop='ratingValue').get_text()

    print(title)

    film['title'] = title
    film['summary'] = summary_text
    film['rating'] = rating

    return film


def create_films_csv(films):
    # write to a csv called film_stats.csv

    path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Scraping_imdb\film_stats.csv'
    
    with open(path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'summary', 'rating']) # create the csv column titles

        for film in films:
            # add the film's title, summary, rating to the csv

            title = film['title'].encode('utf-8')
            summary = film['summary'].encode('utf-8')
            rating = film['rating'].encode('utf-8')

            writer.writerow([title, summary, rating])


def main():
    urls = ['https://www.imdb.com/title/tt0451279/', 'https://www.imdb.com/title/tt5788792/']
    films = []

    for url in urls:
        time.sleep(5) # add a delay in our requests
        film = get_film_stats(url)
        films.append(film)

    create_films_csv(films)

    print('Done processing film URLs.')


if __name__ == "__main__":
    main()

