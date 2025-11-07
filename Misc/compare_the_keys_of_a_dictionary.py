'''
To compare the keys of a dictionary (which are strings) and group the ones that are almost the same, 
you can use string similarity measures such as Levenshtein distance or other fuzzy matching techniques. 

This script will output groups of keys that are similar to each other based on the Levenshtein 
distance being less than or equal to the specified threshold. You can adjust the threshold as needed to control the level of similarity.
'''

from collections import defaultdict
import Levenshtein

'''
my_dict = {
   "CataS + Cip + Darius + Horatiu + Ionut + Tudor": "36.5",
   "Adi + LiviuU + Luci + Robin + Silviu + Stefan": "36.67",
   "CataS + Darius + Horatiu + Ionut + LiviuBrutaru + Tudor": "36.72",
   "AdiBeck + Cip + LiviuU + Luci + Ovidiu + Stefan": "36.47",
   "Adi + Ionut + LiviuBrutaru + Luci + Ovidiu + Silviu": "37.17",
   "Darius + Horatiu + LiviuU + Stefan + Stefan + Tudor": "36.72",
   "CataS + Darius + LiviuBrutaru + LiviuU + Luci + Ovidiu": "37.05",
   "AdiBeck + Cip + CristiH + Ionut + Stefan + Tudor": "37",
   "CataS + Darius + Horatiu + LiviuU + Stefan + Tudor": "36.72",
   "AdiBeck + CristiH + LiviuBrutaru + LiviuU + Luci + Stefan": "37.5",
   "Adi + Cip + Ionut + Ovidiu + Robin + Tudor": "37.8",
   "Adi + AdiBeck + Ionut + LiviuU + Silviu + Tudor": "37.4",
   "CataS + Darius + George + Luci + Ovidiu + Stefan": "37.45",
   "CataS + CristiH + LiviuU + Silviu + Stefan + Tudor": "37.4",
   "Adi + Cip + Darius + Ionut + Luci + Robin": "37.35",
   "Adi + LiviuU + Manu + Ovidiu + Tudor": "31.7",
   "Cip + CristiH + George + Ionut + Vasile": "31.9",
   "CataS + Darius + Horatiu + LiviuBrutaru + Stefan": "31.7",
   "Adi + Cip + LiviuBrutaru + LiviuU + Stefan + Tudor": "37.1",
   "CataS + CristiH + Darius + Horatiu + Luci + Silviu": "37.02",
   "Cip + CristiH + Horatiu + Luci + Silviu + Stefan": "37.1",
   "Adi + CataS + LiviuBrutaru + LiviuU + Tudor": "37.22",
   "Cip + Darius + George + Ionut + LiviuBrutaru + Luci": "37.4",
   "Adi + CataS + CristiH + Horatiu + LiviuU + Tudor": "37.22",
   "Adi + Cip + Ionut + Luci + Silviu + Stefan": "37.15",
   "AdiBeck + CataS + George + Horatiu + LiviuBrutaru + Tudor": "36.97",
   "Adi + Cip + George + Ionut + LiviuBrutaru + Tudor": "37.4",
   "Horatiu + LiviuU + Luci + Robin + Silviu + Stefan": "37.2",
   "Cip + Horatiu + LiviuU + Silviu + Stefan + Tudor": "37.2",
   "Adi + George + Ionut + LiviuBrutaru + Luci + Robin": "37.45",
   "CristiH + George + Horatiu + LiviuBrutaru + Luci + Stefan": "37.6",
   "Adi + Cip + Ionut + MariusM + Silviu + Tudor": "37.65",
   "Adi + Cip + CristiH + Ionut + MariusM + Tudor": "38.21",
   "CataS + Cristi2 + George + Horatiu + LiviuU + Stefan": "38.12",
   "CataS + CristiH + LiviuU + Ovidiu + Silviu + Stefan": "38.37",
   "Darius + Horatiu + Ionut + LiviuBrutaru + MariusM + Tudor": "38.46",
   "Ionut + LiviuBrutaru + Luci + MariusM + Ovidiu + Robin": "38.05",
   "Adi + Darius + Horatiu + LiviuU + Stefan + Tudor": "38.11",
   "CristiH + Horatiu + Ionut + LiviuBrutaru + Robin + Tudor": "37.51",
   "CataS + LiviuU + Luci + MariusM + Ovidiu + Stefan": "37.74",
   "AdiBeck + Darius + Horatiu + LiviuU + Timi + Tudor": "37.61",
   "CataS + CristiH + Ionut + Luci + MariusM + Robin": "37.44",
   "Adi + CataS + Darius + Horatiu + LiviuBrutaru + Silviu": "37.79",
   "Ionut + LiviuU + MariusM + Robin + Stefan + Tudor": "38.11",
   "CataS + Cip + Darius + Horatiu + Ionut + LiviuBrutaru": "37.94",
   "Adi + George + LiviuU + MariusM + Stefan + Tudor": "38.21",
   "Adi + CristiH + Darius + George + Robin + Timi": "38.6",
   "Ionut + LiviuBrutaru + MariusM + Silviu + Stefan + Tudor": "38.31",
   "AdiBeck + CristiH + LiviuU + Ovidiu + Stefan + Tudor": "38.46",
   "Adi + CataS + Cip + Darius + Ionut + MariusM": "38.64",
   "AdiBeck + CristiH + Ionut + MariusM + Stefan + Tudor": "38.81",
   "Adi + CataS + Cip + Darius + LiviuU + Ovidiu": "38.59",
   "AdiBeck + Cip + Darius + MariusM + Ovidiu + Tudor": "38.56",
   "Adi + CataS + CristiH + Ionut + LiviuU + Stefan": "38.84",
   "Cip + Darius + George + Horatiu + LiviuU + Manu": "38.65",
   "Adi + CristiH + LiviuBrutaru + MariusM + Stefan + Tudor": "38.41",
   "Cip + Ionut + LiviuU + MariusM + Stefan + Tudor": "38.46",
   "Adi + CataS + CristiH + Darius + Horatiu + LiviuBrutaru": "38.2"
}
'''

# Sample dictionary
#my_dict = {'apple': 1, 'banana': 2, 'apples': 3, 'bananna': 4, 'orange': 5}

my_dict = {
   "CataS + Cip + Darius + Horatiu + Ionut + Tudor": "36.5",
   "Adi + LiviuU + Luci + Robin + Silviu + Stefan": "36.67",
   "CataS + Darius + Horatiu + Ionut + LiviuBrutaru + Tudor": "36.72",
   "AdiBeck + Cip + LiviuU + Luci + Ovidiu + Stefan": "36.47",
   "Adi + Ionut + LiviuBrutaru + Luci + Ovidiu + Silviu": "37.17",
   "Darius + Horatiu + LiviuU + Stefan + Stefan + Tudor": "36.72",
   "CataS + Darius + LiviuBrutaru + LiviuU + Luci + Ovidiu": "37.05",
   "AdiBeck + Cip + CristiH + Ionut + Stefan + Tudor": "37",
   "CataS + Darius + Horatiu + LiviuU + Stefan + Tudor": "36.72",
   "AdiBeck + CristiH + LiviuBrutaru + LiviuU + Luci + Stefan": "37.5",
   "Adi + Cip + Ionut + Ovidiu + Robin + Tudor": "37.8",
   "Adi + AdiBeck + Ionut + LiviuU + Silviu + Tudor": "37.4",
   "CataS + Darius + George + Luci + Ovidiu + Stefan": "37.45",
   "CataS + CristiH + LiviuU + Silviu + Stefan + Tudor": "37.4",
   "Adi + Cip + Darius + Ionut + Luci + Robin": "37.35",
   "Adi + LiviuU + Manu + Ovidiu + Tudor": "31.7",
   "Cip + CristiH + George + Ionut + Vasile": "31.9",
   "CataS + Darius + Horatiu + LiviuBrutaru + Stefan": "31.7",
   "Adi + Cip + LiviuBrutaru + LiviuU + Stefan + Tudor": "37.1",
   "CataS + CristiH + Darius + Horatiu + Luci + Silviu": "37.02",
   "Cip + CristiH + Horatiu + Luci + Silviu + Stefan": "37.1",
   "Adi + CataS + LiviuBrutaru + LiviuU + Tudor": "37.22",
   "Cip + Darius + George + Ionut + LiviuBrutaru + Luci": "37.4",
   "Adi + CataS + CristiH + Horatiu + LiviuU + Tudor": "37.22",
   "Adi + Cip + Ionut + Luci + Silviu + Stefan": "37.15",
   "AdiBeck + CataS + George + Horatiu + LiviuBrutaru + Tudor": "36.97",
   "Adi + Cip + George + Ionut + LiviuBrutaru + Tudor": "37.4",
   "Horatiu + LiviuU + Luci + Robin + Silviu + Stefan": "37.2",
   "Cip + Horatiu + LiviuU + Silviu + Stefan + Tudor": "37.2",
   "Adi + George + Ionut + LiviuBrutaru + Luci + Robin": "37.45",
   "CristiH + George + Horatiu + LiviuBrutaru + Luci + Stefan": "37.6",
   "Adi + Cip + Ionut + MariusM + Silviu + Tudor": "37.65",
   "Adi + Cip + CristiH + Ionut + MariusM + Tudor": "38.21",
   "CataS + Cristi2 + George + Horatiu + LiviuU + Stefan": "38.12",
   "CataS + CristiH + LiviuU + Ovidiu + Silviu + Stefan": "38.37",
   "Darius + Horatiu + Ionut + LiviuBrutaru + MariusM + Tudor": "38.46",
   "Ionut + LiviuBrutaru + Luci + MariusM + Ovidiu + Robin": "38.05",
   "Adi + Darius + Horatiu + LiviuU + Stefan + Tudor": "38.11",
   "CristiH + Horatiu + Ionut + LiviuBrutaru + Robin + Tudor": "37.51",
   "CataS + LiviuU + Luci + MariusM + Ovidiu + Stefan": "37.74",
   "AdiBeck + Darius + Horatiu + LiviuU + Timi + Tudor": "37.61",
   "CataS + CristiH + Ionut + Luci + MariusM + Robin": "37.44",
   "Adi + CataS + Darius + Horatiu + LiviuBrutaru + Silviu": "37.79",
   "Ionut + LiviuU + MariusM + Robin + Stefan + Tudor": "38.11",
   "CataS + Cip + Darius + Horatiu + Ionut + LiviuBrutaru": "37.94",
   "Adi + George + LiviuU + MariusM + Stefan + Tudor": "38.21",
   "Adi + CristiH + Darius + George + Robin + Timi": "38.6",
   "Ionut + LiviuBrutaru + MariusM + Silviu + Stefan + Tudor": "38.31",
   "AdiBeck + CristiH + LiviuU + Ovidiu + Stefan + Tudor": "38.46",
   "Adi + CataS + Cip + Darius + Ionut + MariusM": "38.64",
   "AdiBeck + CristiH + Ionut + MariusM + Stefan + Tudor": "38.81",
   "Adi + CataS + Cip + Darius + LiviuU + Ovidiu": "38.59",
   "AdiBeck + Cip + Darius + MariusM + Ovidiu + Tudor": "38.56",
   "Adi + CataS + CristiH + Ionut + LiviuU + Stefan": "38.84",
   "Cip + Darius + George + Horatiu + LiviuU + Manu": "38.65",
   "Adi + CristiH + LiviuBrutaru + MariusM + Stefan + Tudor": "38.41",
   "Cip + Ionut + LiviuU + MariusM + Stefan + Tudor": "38.46",
   "Adi + CataS + CristiH + Darius + Horatiu + LiviuBrutaru": "38.2"
}

# Define a threshold for similarity
threshold = 9

# Group similar keys
groups = defaultdict(list)

for key1 in my_dict:
    for key2 in my_dict:
        if key1 != key2 and Levenshtein.distance(key1, key2) <= threshold:
            groups[key1].append(key2)

# Print the groups
for key, similar_keys in groups.items():
    print(f"Keys similar to '{key}': {similar_keys}")