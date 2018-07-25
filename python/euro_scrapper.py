import collections
import datetime
import os
from bs4 import BeautifulSoup

archive_results = dict()
url_archive_page = "https://www.euro-millions.com/results-archive-"
url_file_text = "/Historical_data/EuroMillions_Results_Archive_for_"


def get_years():
    now = datetime.datetime.now()
    return [str(year_of_draw) for year_of_draw in range(2004, now.year + 1)]


def get_historical_results(url):
    soup = BeautifulSoup(open(url), 'html.parser')
    all_archive_divs = soup.find_all(class_='archives')
    for div in all_archive_divs:
        draw_date = datetime.datetime.strptime(div.find('a')['href'][-10:],
                                               "%d-%m-%Y").date()
        lotto_numbers = []
        euro_uls = div.select('ul')[0]  # [0] will exclude euro plus
        for ball in euro_uls.find_all('li', {'class': 'ball'}):
            lotto_numbers.append(int(ball.get_text()))

        bonus_numbers = []
        for ball in div.find_all('li', {'class': 'lucky-star'}):
            bonus_numbers.append(int(ball.get_text()))

        # Euro Plus 1st Draw:: 2007-06-15
        plus_numbers = []
        try:
            plus_uls = div.select('ul')[1]  # [1] will get euro plus
            for ball in plus_uls.find_all('li', {'class': 'ball'}):
                plus_numbers.append(int(ball.get_text()))
        except IndexError:
            plus_uls = 'null'

        archive_results[draw_date] = {'lotto_nums': lotto_numbers,
                                      'bonus_nums': bonus_numbers,
                                      'euro_plus': plus_numbers}

    return archive_results


def order_dictionary(dictionary):
    return collections.OrderedDict(sorted(dictionary.items()))


def display_historical_results(dictionary):
    for dates, numbers in dictionary.items():
        print("{} {}".format(dates, numbers))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    for draw_year in get_years():
        url_year = os.getcwd() + url_file_text + "{}.html".format(draw_year)
        get_historical_results(url_year)

    results_dict = order_dictionary(archive_results)
    display_historical_results(results_dict)
    print("Total Number of Draws:: {}".format(len(results_dict)))
    print("Total Time to retrieve the data:: {}".format(
        datetime.datetime.now() - start_time))
