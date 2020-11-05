from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r"C:\Users\82105\Desktop\map\chromedriver")
driver.get("https://map.kakao.com/")

elem = driver.find_element_by_id("search.keyword.query")

elem.clear()

elem.send_keys("황태자베이커리")

elem = driver.find_element_by_id("search.keyword.submit")

elem.click()

print(location)


################################################################################
# import sys
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# SEARCH = "사직동 하이데이지"
# TIMEOUT = 5

# driver = None
# try:
#     driver = webdriver.Chrome(r"C:\Users\82105\Desktop\map\chromedriver")
#     driver.set_window_size(1200, 800)
#     # 1) search
#     driver.get("https://map.kakao.com/")
#     driver.implicitly_wait(TIMEOUT)
#     # 검색 엘리먼트를 찾아 검색어를 입력하고
#     elem = driver.find_element_by_id("search.keyword.query")
#     elem.send_keys(SEARCH)
#     # 검색 단추를 누른다
#     elem = driver.find_element_by_id("search.keyword.submit")
#     elem.click()

#     # 2) get result list
#     for ndx in range(100):
#         driver.implicitly_wait(TIMEOUT)
#         # 현재 검색 목록에 대해 목록의 상위에 해당하는 엘리먼트를 구해옴 (기다렸다)
#         elem = driver.find_element_by_class_name('widget-pane-content-holder')
#         dt = elem.find_element_by_xpath('.//div/div[@role="listbox"]')
#         rd = {}
#         try:
#             # 검색 결과 중에 ndx 번째 결과의 엘리먼트를 구해옴
#             d = dt.find_element_by_xpath('.//div[@data-result-index="%s"]' % ndx)
#             lines = d.text.split('\n')
#             # 첫번째 줄은 호텔이름
#             rd['hotel'] = lines[0]
#             # 나머지 줄은 정보로
#             rd['info'] = ','.join(lines[1:])
#             # 해당 정보를 눌러 상세 정보 보기
#             d.click()
#             # 다음 몇초를 쉬는 이유는 아래의 elem 이나 back_button 등을
#             # WebDriverWait로 구해와도 ElementNotVisibleException 등의 예외 때문
#             # (아마도 지도에 표시를 하는 등 data binding 시간이 꽤 걸리는 듯)
#             driver.implicitly_wait(TIMEOUT)
#             # 상세 정보 엘리먼트 구해옴 (기다리며)
#             elem = driver.find_element_by_class_name('widget-pane-content-holder')
#             # 주소 구해옴 : 생략될 수 있기 때문에 try
#             try:
#                 it = elem.find_element_by_xpath('.//div/div[@data-section-id="ad"]')
#                 rd['address'] = it.text
#             except Exception:
#                 pass
#             # 홈페이지 구해옴 : 생략될 수 있기 때문에 try
#             try:
#                 it = elem.find_element_by_xpath('.//div/div[@data-section-id="ap"]')
#                 rd['homepage'] = it.text
#             except Exception:
#                 pass
#             # phone 구해옴 : 생략될 수 있기 때문에 try
#             try:
#                 it = elem.find_element_by_xpath('.//div/div[@data-section-id="pn0"]')
#                 rd['phone'] = it.text
#             except Exception:
#                 pass
#             print(rd)
#             # 이전 "검색결과로 돌아가기" 누름
#             back_button = elem.find_element_by_xpath('.//div/button')
#             back_button.click()
#         except NoSuchElementException:
#             # 검색 결과 중에 구해오기 위한 ndx 번째를 너머서면 못구하고 해당 오류가
#             # 발생하므로 for loop 빠짐
#             break   # End of list
#         except Exception:
#             raise

# finally:
#     # quit
#     if driver is not None:
#         driver.quit()





# options = webdriver.ChromeOptions()
# options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
# options.add_argument('disable-gpu')    # GPU 사용 안함
# options.add_argument('lang=ko_KR')    # 언어 설정
# driver = webdriver.Chrome(chromedriver, options=options) #  옵션 적용


















# import requests
# import pprint

# # 검색할 주소
# location = '서현동'

# # 요청 주소(구글맵)

# # Local(테스트) 환경 - https 요청이 필요없고, API Key가 따로 필요하지 않지만 횟수에 제약이 있습니다.
# URL = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address={}' \
# .format(location)

# # Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
# # URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=<구글 맵 API key>' \
# # '&sensor=false&language=ko&address={}'.format(location)

# # URL로 보낸 Requst의 Response를 response 변수에 할당
# response = requests.get(URL)

# # JSON 파싱
# data = response.json()

# # lat, lon 추출
# lat = data['results'][0]['geometry']['location']['lat']
# lng = data['results'][0]['geometry']['location']['lng']

# # print() 함수 대신 pprint.pprint() 함수를 사용하는 이유는 좀 더 보기 쉽게 출력하기 위함입니다.
# pprint.pprint(data)