from selenium import webdriver

def getNugPrices():

    driver = webdriver.Chrome(executable_path=r'C:\Users\Liam\Documents\PersonalProjects\Discord Bots\chromedriver.exe')
    driver.get('https://www.fastfoodmenuprices.com/mcdonalds-prices/')


    menu = driver.find_elements_by_tag_name('tr')
    nuggets = "McNuggets"
    nuggs = ''

    print(len(menu))
    for item in menu:
        if (item.text.find(nuggets) != -1):
            nuggs += (item.text + '\n')

    driver.quit()
    return nuggs

