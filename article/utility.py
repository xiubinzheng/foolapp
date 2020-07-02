import json

content_file = 'data_content/content_api.json'

def get_articles_via_content_api():
    with open(content_file) as content_json_file:
        content_data = json.load(content_json_file)
    content_json_file.close()
    return content_data.get('results')


def get_homepage_article():
    articles_list = get_articles_via_content_api()

    for article in articles_list:
        for item in article['tags']:
            if item['slug'] == '10-promise':
                    return article