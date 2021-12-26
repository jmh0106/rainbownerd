import time
from requests.utils        import quote
from urllib                import parse
from selenium              import webdriver
WAIT_TIME_TO_LOAD = 10

lol_dict = {
    'cham_name'   : '',
    'cham_tier'   : '',
    'cham_honey'  : False,
    'cham_op'     : True,

    'win_rate'    : '',
    'pick_rate'   : '',
    'ban_rate'    : '',

    'main_rune' : [],
    'sub_rune'  : [],
    'frag_rune' : [],

    'summoner_spell' : [], 

    'start_item' : [],

    'core_item' : [],
    'boots_item' : '',

    'skill_master' : [],
}
 
# 찾을 챔피언 검색
lol_dict['cham_name'] = "베인"
URL = "https://lol.ps/search/?q=" + quote("베인")

# 셀레니움 크롤링 실행
driver = webdriver.Chrome(executable_path = 'chromedriver')
driver.implicitly_wait(WAIT_TIME_TO_LOAD)
driver.get(url = URL)
driver.maximize_window()

chamBuild = driver.find_element_by_xpath("/html/body/main/div[1]/section")
chamBuildImage = chamBuild.screenshot_as_png
with open('test.png', 'wb') as file:
    file.write(chamBuildImage)