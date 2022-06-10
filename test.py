import random

# 단어 저장 리스트
userDictionary = ["apple:사과", "banana:바나나", "car:자동차", "dice:주사위"]
# 유저 입력 저장 변수
userCommand = ""

print("12223916 정민호의 단어장 프로그램입니다.")

# 종료가 나와서 [break] 될 때까지 실행
while (True):
    print("=" * 50)
    # 유저의 입력 받기
    userCommand = input("추가, 삭제, 확인, 시험, 종료 : ")

    # 유저의 입력을 받아 사전에 추가하기
    if userCommand == "추가":
        userDictionary.append(input("[영어:한국어] 형태로 입력해주세요 : "))

    # 단어의 번호를 받아서 리스트에서 인덱스로 제거하기
    elif userCommand == "삭제":
        wordNum = int(input("삭제하실 단어의 번호를 입력해주세요 : ")) - 1
        print("[", userDictionary[wordNum], "]", " 단어를 삭제하였습니다.")
        del userDictionary[wordNum]

    # for문을 사용해 리스트를 전부 출력하기
    elif userCommand == "확인":
        for i in userDictionary:
            print(str(userDictionary.index(i) + 1) + ") " + i)

    # 리스트에 있는 단어를 :기준으로 나누고 정답일 경우 점수를 올리고 정답률을 출력함
    elif userCommand == "시험":
        Score = 0
        copyUserDictionary = userDictionary
        random.shuffle(copyUserDictionary)
        print("영단어가 나오면 단어의 뜻을 한국어로 적으세요.")
        for i in copyUserDictionary:
            KoreanWord, EngWord = i.split(":")[0], i.split(":")[1]
            if EngWord == input(KoreanWord + " : "):
                Score += 1
        print(Score , "/", len(userDictionary), ":", str(Score / len(userDictionary) * 100) + "%")

    # 프로그램 종료
    elif userCommand == "종료":
        break

    # 유효하지 않은 명령어
    else:
        print("유효하지 않은 명령어입니다.")