import requests
from bs4 import BeautifulSoup

_url = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
source = requests.get(_url).text
soup = BeautifulSoup(source, "html.parser")

DataDay = soup.select_one("#content > div > div:nth-child(7) > table > thead > tr > th:nth-child(8)").get_text()
KoreanConfirmedPlus = soup.select_one("#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(8)").get_text()
KoreanConfirmedAllMale = soup.select_one("#content > div > div:nth-child(28) > table > tbody > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1)").get_text()
KoreanConfirmedAllFemale = soup.select_one("#content > div > div:nth-child(28) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1)").get_text()
KoreanDeadPlus = soup.select_one("#content > div > div:nth-child(7) > table > tbody > tr:nth-child(1) > td:nth-child(8)").get_text()
KoreanDeadAllMale = soup.select_one("#content > div > div:nth-child(28) > table > tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)").get_text()
KoreanDeadAllFemale = soup.select_one("#content > div > div:nth-child(28) > table > tbody > tr:nth-child(2) > td:nth-child(3) > span:nth-child(1)").get_text()

print(DataDay,KoreanConfirmedPlus , KoreanDeadAllMale, KoreanDeadAllFemale, KoreanDeadPlus, KoreanDeadAllMale, KoreanDeadAllFemale)