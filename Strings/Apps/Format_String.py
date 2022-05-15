band_name = input('Please, enter a band name:\n')
formated_band_name = band_name.replace(' ', '+')
print(f'Searching {band_name}. Wait, please...')
base_url = 'http://www.best-cd-price.co.uk'
search_url = f'http://www.best-cd-price.co.uk/search-Keywords/1-/229816/{formated_band_name}.html'

print(search_url)
