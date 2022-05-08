
import os
import time

from selenium import webdriver
path = os.path.join(os.getcwd(),'chromedriver')


def get_article_links():
    global path
    driver = webdriver.Chrome(executable_path=path)
    main_xpath = "/html/body/div[8]/div/div/div/div[1]/a"
    driver.get("https://deerwalk.edu.np/sifalschool/StudentCorner/view/5")
    links = driver.find_elements_by_xpath(main_xpath)
    links_main = []
    for link in links:
        links_main.append(link.get_attribute('href'))

    with open('links.txt','w') as writer:
        for link in links_main:
            writer.write(link+'\n')

    print("DONE GETTING LINKS")


def main():
    with open('links.txt','r') as reader:
        links = reader.readlines()
    global path
    article_xpath = "//*[@id=\"BRR\"]/div[2]/p"
    id_s = [ x.split('/')[-1].strip('\n') for x in links ]
    driver = webdriver.Chrome(executable_path=path)
    for i in range(0,len(id_s)):
        driver.get(links[i])
        data = driver.find_elements_by_xpath(f'//*[@id="{id_s[i]}"]/div[2]/p')
        # print(data.text)
        for d in data :
            print(d.text)
            with open(f'articles/{i}_.txt','a') as writer:
                writer.write(d.text+'\n')

        # datas = [d.text for d in data]

    # print(datas)

    

if __name__ == '__main__':
    get_article_links() # gets harek article ko link
    main() # gets article content and wirtes to txt file

