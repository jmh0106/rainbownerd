import random, sys

userCommand = ""
userDictionaryArray = []
currentUserDictionary = None

class Dict:
    def __init__(self, _name):
        self.dicName = _name
        self.userDictionary = []

    def addWord(self, _word):
        self.userDictionary.append(_word)

    def delWord(self, _index):
        print("[", self.userDictionary[_index], "] 단어가 삭제되었습니다.")
        del self.userDictionary[_index]
    
    def seeWords(self):
        for i in self.userDictionary:
            print(str(self.userDictionary.index(i) + 1) + ") " + i)

    def testWords(self):
        score = 0
        copyUserDictionary = self.userDictionary.copy()
        random.shuffle(copyUserDictionary)
        print("영단어가 나오면 단어의 뜻을 한국어로 적으세요.")
        for i in copyUserDictionary:
            korWord, engWord = i.split(":")[0], i.split(":")[1]
            if engWord == input(korWord + " : "):
                score += 1
        print(score , "/", len(copyUserDictionary), ":", str(score / len(copyUserDictionary) * 100) + "%")

def makeDictionary(_name):
    print("[", _name, "] 단어장이 생성되었습니다.")
    userDictionaryArray.append(Dict(_name))

def changeDictionary(_index):
    global currentUserDictionary
    currentUserDictionary = userDictionaryArray[_index]

def delDictionary(_index):
    print("[", userDictionaryArray[_index].dicName, "] 단어장이 삭제되었습니다.")
    del userDictionaryArray[_index]

def showDictionarys():
    for i in userDictionaryArray:
        print(str(userDictionaryArray.index(i) + 1) + ") " + i.dicName)

print("12223916 정민호의 단어장 프로그램")

while(True):
    if currentUserDictionary == None:
        if len(userDictionaryArray) == 0:
            print("=" * 25, "단어장 관리 메뉴", "=" * 25)
            makeDictionary(input("단어장을 새로 생성합니다. 사용할 단어장의 이름을 입력해주세요 : " ))
        
        while (True):
            print("=" * 25, "단어장 관리 메뉴", "=" * 25)
            userCommand = input("추가, 삭제, 확인, 선택, 종료 : ")

            if userCommand == "추가":
                makeDictionary(input("단어장을 새로 생성합니다. 사용할 단어장의 이름을 입력해주세요 : " ))
            
            elif userCommand == "삭제":
                showDictionarys()
                delDictionary(int(input("삭제할 단어장의 번호를 입력해주세요 : ")) - 1)
            
            elif userCommand == "확인":
                showDictionarys()

            elif userCommand == "선택":
                showDictionarys()
                changeDictionary(int(input("사용할 단어장을 선택해주세요 : ")) - 1)
                break

            elif userCommand == "종료":
                sys.exit(0)

    print("=" * 25, currentUserDictionary.dicName + " 단어장", "=" * 25)
    userCommand = input("추가, 삭제, 확인, 시험, 종료 : ")

    if userCommand == "추가":
        currentUserDictionary.addWord(input("[영어:한국어] 형태로 입력해주세요 : "))
    
    elif userCommand == "삭제":
        currentUserDictionary.delWord(int(input("삭제하실 단어의 번호를 입력해주세요 : ")) - 1)
    
    elif userCommand == "확인":
        currentUserDictionary.seeWords()

    elif userCommand == "시험":
        currentUserDictionary.testWords()
    
    elif userCommand == "종료":
        currentUserDictionary = None