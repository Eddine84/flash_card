# import requests
# from bs4 import BeautifulSoup

# URL = "https://quotes.toscrape.com/tag/love/"

# response = requests.get(URL)


# soup = BeautifulSoup(response.text,"html.parser")

# qutes_class = soup.find_all("div", class_="quote")

# for quote in qutes_class:
#     autothor = quote.find("small",class_="author")
#     text_aitho = quote.find("span", class_="text")
#     print(f"{autothor.text},said :{text_aitho.text}")

# tag_dictionnaire = {}
# for quote in qutes_class:
#     tags = quote.find_all("a", class_="tag")
#     for tag in tags:
#         tag_text = tag.text
#         if tag_text not in tag_dictionnaire:
#             tag_dictionnaire[tag_text] = 0
#         tag_dictionnaire[tag_text]+=1

# print(tag_dictionnaire)










import requests
from bs4 import BeautifulSoup

#get site
web_site_countries = requests.get("https://www.scrapethissite.com/pages/simple/")

# scrapping

countries_text_web = BeautifulSoup(web_site_countries.text, "html.parser")



countries = countries_text_web.find_all("div",class_="country")

data = {}

for country in countries:
    country_name_text = country.find("h3" , class_="country-name").get_text(strip=True)
    capital_name_text = country.find("span", class_="country-capital").get_text(strip=True)
    country_population_text = country.find("span", class_="country-population").get_text(strip=True)
    country_area_text = country.find("span", class_="country-area").get_text(strip=True)
    if capital_name_text != "" or "population" > 0 or "area" > 0:
        country_data = {
            "capital" :capital_name_text,
            "population" :country_population_text,
            "area":country_area_text
        }
        data[country_name_text] = country_data


total_countries = 0
area = 0
population = 0
max_population_data = {

}
min_count = 0
min_inital_lenth = 0
max_inital_lenth = float('inf')
max_count = float("inf")
country_heighst_result = {}
country_min_result = {}
shorted_country_name = ""
longest_country_name = ""
for country ,country_data in data.items():
    value_number_area = float(country_data["area"])
    value_number_population = int(country_data["population"])
    area +=value_number_area
    population  +=value_number_population
    total_countries+=1
    num_popultation = int(country_data["population"])
    country_name_lenth = len(country)
    if num_popultation > min_count:
        min_count = num_popultation
        country_heighst_result["country"] = country
    if num_popultation < max_count:
        max_count = num_popultation
        country_min_result["country"] = country

    if min_inital_lenth < country_name_lenth:
        min_inital_lenth = country_name_lenth
        shorted_country_name = country

    if max_inital_lenth > country_name_lenth:
        max_inital_lenth = country_name_lenth
        longest_country_name = country
    


total_area = area
average = population / total_countries


print(f"1.\tThe total area of all the countries is\t\t\t: {total_area} km2")


# 2. Compute the total population of all the countries
total_population = population
print(f"2.\tThe total population of all the countries is\t\t: {total_population}")


# 3. total off all countries
print(f"2.\tThe total  of all the countries is\t\t: {total_countries}")


# 5. Compute the average population of all the countries
average_population = average
print(f"5.\tThe average population of all the countries is\t\t: {average_population}")


# 6. Compute the average population density of all the countries
average_population_density = population / area
print(f"6.\tThe average population density of all the countries is\t: {average_population_density}")

# 7. Compute the country with the highest population

print(country_heighst_result)
print(country_min_result)
print(shorted_country_name)
print(longest_country_name)


