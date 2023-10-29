from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


def get_source_html():
    o = Options()
    o.add_experimental_option("detach", True)
    cService = Service(executable_path=r'C:\Users\Администратор\Desktop\Проекты\chromedriver\chromedriver-win64'
                                       r'\chromedriver.exe')
    o.add_argument("user-data-dir=C:\\profile")
    driver = wd.Chrome(service=cService, options=o)

    driver.get('https://auto.ru/slantsy/cars/all/?price_from=250000&price_to=450000')
    sleep(3)

    with open('source-page.html', 'w', encoding='utf8') as file:
        file.write(driver.page_source)


# button = driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Anchor")
# button.click()
# sleep(5)

def get_info_cars(file_path):
    with open(file_path, encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cars_card = soup.find_all('div', class_="ListingItem ListingItem_ctbautoru128Exp")
    crs = []
    for cars in cars_card:
        car_name = cars.find('a', class_="Link ListingItemTitle__link").text
        crs.append(car_name)
        car_price = cars.find('div', class_="ListingItemPriceNew__content-HAVf2").text
        car_price = car_price.replace('\xa0', '')
        crs.append(car_price)
        car_link = cars.find('a', class_="Link ListingItemTitle__link").get('href')
        crs.append(car_link)

    with open(r'C:\Users\Администратор\PycharmProjects\sniffer_bot\pars_cars.txt', 'w', encoding='utf8') as file:
        for car in crs:
            file.write(f'{car}\n')


def main1():
    get_source_html()
    get_info_cars(file_path=r'C:\Users\Администратор\PycharmProjects\sniffer_bot\source-page.html')


if __name__ == '__main__':
    main1()
