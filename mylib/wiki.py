import wikipedia
from yake import KeywordExtractor

# build a function to return a summary of a wikipedia page given a city name
def get_city_summary(city):
    """Get a summary of a wikipedia page given a city name

    :param city: The name of the city
    :return: A summary of the wikipedia page
    """
    try:
        return wikipedia.summary(city)
    except wikipedia.exceptions.PageError:
        return "City not found on Wikipedia"


# build a function to search for a match of page on wikipedia
def search_wiki_pages(page):
    """Search for a match of page on wikipedia

    :param page: The name of the page
    :return: A list of matches
    """
    return wikipedia.search(page)


# build a function to get the full page of a wikipedia page given a page name
def get_wiki_page(page):
    """Get the full page of a wikipedia page given a page name

    :param page: The name of the page
    :return: A full page of the wikipedia page
    """
    try:
        return wikipedia.page(page).content
    except wikipedia.exceptions.PageError:
        return "City not found on Wikipedia"


# return a list of keywords from a wikipedia page
def get_wiki_keywords(page):
    """Return a list of keywords from a wikipedia page

    :param page: The name of the page
    :return: A list of keywords
    """
    try:
        content = get_wiki_page(page)
        kw_extractor = KeywordExtractor()
        keywords = kw_extractor.extract_keywords(content)
        # return the top 10 keywords
        return {keyword: score for keyword, score in keywords[:10]}
    except wikipedia.exceptions.PageError:
        return "City not found on Wikipedia"
