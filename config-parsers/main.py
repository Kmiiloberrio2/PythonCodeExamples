import common
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)

# logger = logging.getLogger(__name__)


def _news_scraper(new_site):
    host = common.config_yaml()['news_sites'][new_site]['url']
    logging.info(f'Beginning scraper for {host}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    new_site_choices = list(common.config_yaml()['news_sites'].keys())
    parser.add_argument('news_site', help='The news site that you want to scrape', type=str, choices=new_site_choices)

    args = parser.parse_args()
    # print(args)
    _news_scraper(args.news_site)
