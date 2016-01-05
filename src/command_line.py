"""
    command-line control for site scrappers

"""

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Kickass Command-line Interface: scraping torrents accelerated')
    parser.add_argument('--category', metavar='FIELD', 
                        choices=['movies', 'books', 'music', 'anime', 'games', 'tv', 'new', 'xxx', 'apps', 'other', 'all'],
                        default='movies', help='Get the specific category. "all" category only works when using --search')
    parser.add_argument('--magnet2file', action='store_true', default=False,
                        help='output the magnet links in file')
    parser.add_argument('--csvfile', action='store_true', default=False,
                        help='output the data in csv file')
    parser.add_argument('--counts', type=int, default=25,
                        help='number of top torrent links to scrap, default 25.')
    parser.add_argument('--search', action='store', dest='keyword', default = None, type = str,
                        help='Search a keyword, replace space with hyphen. Does not work with "other" category.')
    parser.add_argument('--workers', type=int, default=8,
                        help='number of workers to use, 8 by default.')
    return parser.parse_args()

def check_args(options):
    """ check whether input arguments are valid
    """
    if (options.category == 'other' and options.keyword != None):
        raise AssertionError('--search does not work with "other" category.')

    if (options.category == 'all' and options.keyword == None):
        raise AssertionError('"all" category only works when using --search')
