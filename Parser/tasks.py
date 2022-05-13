import requests
from bs4 import BeautifulSoup
import json
from celery import app 
from celery import shared_task
from .models import News


@shared_task(serializer='json')
def save_function(article_list):
    print('starting')

    for article in article_list:
        try:
            print(article)
            print(type(article))
            News.objects.create(
                url = article['url'],
                domain=article['domain'],
                create_date=article['create_date'],
                update_date=article['update_date'],
                country=article['country'],
                is_dead=article['is_dead'],
                a=article['a'],
                ns=article['ns'],
                cname=article['cname'],
                mx=article['mx'],
                txt=article['txt'],
                link_id=article['link_id']
            )
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')


@shared_task
def hackernews_rss(link, link_id):
    article_list = []
    try:
        print('Starting the Scrapping tool')
        r = requests.get(link)
        soup = BeautifulSoup(r.content, features='lxml')
        container = soup.select('a')
        url_storage = []
        for block in container:
            try:
                url1 = block.get('href')
                if url1.startswith('http'):
                    url_storage.append(url1)
            except:
                continue
        for url in url_storage:
            r = requests.get(f'https://api.domainsdb.info/v1/domains/search?domain={url}')
            data = r.text
            parse_json = json.loads(data)
            for block in parse_json['domains']:
                domain = block['domain']
                create_date = block['create_date']
                update_date = block['update_date']
                country = block['country']
                is_dead = block['isDead']
                a = block['A']
                ns = block['NS']
                cname = block['CNAME']
                mx = block['MX']
                txt = block['TXT']
                article = {
                    'url': url,
                    'domain': domain,
                    'create_date': create_date,
                    'update_date': update_date,
                    'country': country,
                    'is_dead': is_dead,
                    'a': a,
                    'ns': ns,
                    'cname': cname,
                    'mx': mx,
                    'txt': txt,
                    'link_id': link_id
                }
                print(article)
                article_list.append(article)
            print('Finished scraping the articles')
            return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)