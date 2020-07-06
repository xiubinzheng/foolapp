import random
import json

content_file = 'data_content/content_api.json'
quote_file = 'data_content/quotes_api.json'


# some thoughts, this method is being called mutliple times,
# it might get expensive as we are calling get_article_via_content_api 
# each time we call get_home_page_article, get_aritcle_by_uuid, get_random_article, 
# another better way of doing this might be to just have the 
# get_articles_via_content_api called once and just pass in the results as 
# a parameter to methods instead, but due to time 
#constraint will leave it like this for now
def get_articles_via_content_api():
    with open(content_file) as content_json_file:
        content_data = json.load(content_json_file)
    content_json_file.close()
    return content_data.get('results')

# get stocks from the api 
def get_stocks_via_content_api():
    with open(quote_file) as quote_json_file:
        quote_data = json.load(quote_json_file)
    quote_json_file.close()
    return quote_data

# look in the articles to find article that 
# has slug of 10-promise and return it
def get_homepage_article():
    articles_list = get_articles_via_content_api()
    for article in articles_list:
        for item in article['tags']:
            if item['slug'] == '10-promise':
                    return article

# grab the article by uuid, pretty straight forward
def get_article_by_uuid(uuid):
    articles_list = get_articles_via_content_api()
    for article in articles_list:
        if article['uuid'] == uuid:
            return article

# get random articles
def get_random_articles(count):
    articles_list = get_articles_via_content_api()
    result = []

    homepage_article = get_homepage_article() 
    # while we have less than 3 or so amount of articles,
    # keep pick a random articles, if the article was already in the 
    # result pick another one instead
    # also check to make sure to exclude homepage_article in the result.
    while len(result) < count:
        item = random.choice(articles_list)
        if item !=homepage_article and item not in result:
            result.append(item)

    return result

# get random stcoks
def get_random_stocks(count):
    stocks_list = get_stocks_via_content_api()
    result = []
    # while we have less than 3 or so amount of stocks,
    # keep pick a random stock, if the stock was already in the 
    # result pick another one instead
    while len(result) < count:
        stock = random.choice(stocks_list)
        if stock not in result:
            result.append(stock)

    return result
