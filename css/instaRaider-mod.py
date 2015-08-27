import requests
import re
import selenium.webdriver as webdriver
import time


def get_video_count(profile_url):
    driver = webdriver.Firefox()
    driver.get(profile_url)

    scroll_to_bottom = get_posts_count(profile_url)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    element = driver.find_element_by_css_selector('div.-cx-PRIVATE-AutoloadingPostsGrid__moreLoadingIndicator a')
    element.click()

    for y in range(int(scroll_to_bottom)):
        scroll_page(driver)

    # After load all profile photos, retur, source to download_photos()
    time.sleep(1)
    source = driver.page_source

    driver.close()

    return source.encode('utf-8')

    '''
    response = requests.get(profile_url)
    counts_code = re.findall(r'\"is_video":true', response.text)
    if not counts_code:
        print "has no videos to download."
    else:
        print "has {} videos available to download.".format(len(counts_code))
    '''


def get_posts_count(profile_url):
        """
        Given a url to Instagram profile, return number of photos posted
        """
        response = requests.get(profile_url)
        counts_code = re.search(r'\"media":{"count":\d+', response.text)
        if not counts_code:
            return None
        return re.findall(r'\d+', counts_code.group())[0]


def scroll_page(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)
        driver.execute_script("window.scrollTo(0, 0);")


def get_scroll_count(count):
        return (int(count) - 24) / 12 + 1

def write_file(source):
    with open("her_source.txt", "w+") as file:
        for line in source:
            file.write(line)

write_file(get_video_count("https://instagram.com/kateupton/"))
