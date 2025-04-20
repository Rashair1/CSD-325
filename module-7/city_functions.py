def city_country(city, country, population=0, language=0):
#convert to strings to make population optional
    output_string = f"{city.title()}, {country.title()}"
#separate population, add dash '-'
    if population:
        output_string += f" - population {population}"
    elif language:
        output_string += f" - language {language}"
    return output_string


# Call the function at least three times
city_country("Houston", "USA")
city_country("Philadelphia", "USA", "1,600,000")
city_country("Los Angeles", "USA", "3.400,000", "English")

