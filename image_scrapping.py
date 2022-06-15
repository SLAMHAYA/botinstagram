import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import karim_data
os.chdir('C:/Users/jorge/OneDrive/Documents/B2/Dev_Final_Project')


# Install driver
opts = webdriver.ChromeOptions()
opts.headless = True
image_db = []
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

search_url = "https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"
driver.get(search_url.format(q='karim benzema'))

# scroll to the end


def scroll_to_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # sleep_between_interactions

# get image url


def getImageUrls(name, totalImgs, driver):
    search_url = "https://www.google.com/search?q=karim+benzema&rlz=1C1CHBF_frFR918FR918&sxsrf=ALiCzsZt8__NU4Z6Zgfl1EPERoDVhkuxkw:1655259981297&source=lnms&tbm=isch&sa=X&ved=2ahUKEwitusj5s674AhUJcxoKHen2D7MQ_AUoAnoECAIQBA&biw=1280&bih=936&dpr=1"
    driver.get(search_url.format(q=name))
    img_urls = set()
    img_count = 0
    results_start = 0

    while(img_count < totalImgs):  # Extract actual images now

        scroll_to_end(driver)

        thumbnail_results = driver.find_elements_by_xpath(
            "//img[contains(@class,'rg_i Q4LuWd')]")
        totalResults = len(thumbnail_results)
        print(
            f"Found: {totalResults} search results. Extracting links from{results_start}:{totalResults}")

        for img in thumbnail_results[results_start:totalResults]:

            img.click()
            time.sleep(2)
            actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
                    img_urls.add(actual_image.get_attribute('src'))

            img_count = len(img_urls)

            if img_count >= totalImgs:
                print(f"Found: {img_count} image links")
                break
            else:
                print("Found:", img_count, "looking for more image links ...")
                load_more_button = driver.find_element_by_css_selector(
                    ".mye4qd")
                driver.execute_script(
                    "document.querySelector('.mye4qd').click();")
                results_start = len(thumbnail_results)
    return img_urls


def downloadImages(folder_path, file_name, url):
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f"ERROR - COULD NOT DOWNLOAD {url} - {e}")
    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')

        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SAVED - {url} - AT: {file_path}")
    except Exception as e:
        print(f"ERROR - COULD NOT SAVE {url} - {e}")


def saveInDestFolder(searchNames, destDir, totalImgs, driver):
    for name in list(searchNames):
        path = os.path.join(destDir, name)
        if not os.path.isdir(path):
            os.mkdir(path)
        print('Current Path', path)
        totalLinks = getImageUrls(name, totalImgs, driver)
        print('totalLinks', totalLinks)

        if totalLinks is None:
            print('images not found for :', name)
            continue
        else:
            for i, link in enumerate(totalLinks):
                file_name = f"{i}.jpg"
                downloadImages(path, file_name, link)
                image = Image.open('./KarimUpload/'+file_name)
                rez_image = image.resize((1080, 1080))
                rez_image.save('./Insta image/'+file_name)
                image_db.append('./Insta image/'+str(i)+'.jpg')


searchNames = ['KarimUpload']
destDir = f'./'
totalImgs = 35

saveInDestFolder(searchNames, destDir, totalImgs, driver)
# INSERT TO DB
karim_data.InsertPublicationToDB(image_db)
