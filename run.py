# -*- coding: utf-8 -*-
#임포트
import asyncio, discord, datetime, requests, urllib, time, random, os

from discord.ext import commands
from selenium import webdriver
from bs4 import BeautifulSoup

#봇 초기 설정
app = discord.Client()

access_token = os.environ["BOT_TOKEN"]
token = access_token

#봇 첫 로그인
@app.event
async def on_ready():
    print("다음으로 로그인 합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("!도움말")
    await app.change_presence(status = discord.Status.online, activity = game)

#메세지 처리
@app.event
async def on_message(message):
    #봇의 메세지라면 리턴
    if message.author.bot:
        return None
    
    #메세지 처리
    param = message.content.split()
    
    if message.content.startswith("!"):
        await message.delete()
    else:
        return None
    
    #!도움말
    if param[0] == "!도움말":
        await message.channel.send(embed = showServerInfo())

    #!시간
    elif param[0] == "!시간":
        if (len(param) == 1):
            await message.channel.send(embed = showTime(0))
        else:
            await message.channel.send(embed = showTime(int(param[1])))

    #!롤
    elif param[0] == "!롤":
        #빌드
        if param[1] == "빌드":
            isError = False

            msg = await message.channel.send(embed = showLOLBuild(param[2]))
        
        #전적
        else:
            userName = userNameChange(message.content)
            countNum = param[len(param) - 1]
            isError = False

            #소환사 이름 검사
            if len(param) < 2:
                msg = discord.Embed(title = "!오류", description = "소환사 이름을 입력해주세요")
                isError = True
            elif param[1] == "북미":
                if len(param) < 3:
                    msg = discord.Embed(title = "!오류", description = "소환사 이름을 입력해주세요")
                    isError = True

            #숫자 유무 검사
            if countNum.isdigit():
                #9 이상, 0일 경우 검사
                if int(countNum) > 9:
                    msg = discord.Embed(title = "!오류", description = "전적은 최대 9개까지 검색하실 수 있습니다")
                    isError = True
                elif int(countNum) == 0:
                    msg = discord.Embed(title = "!오류", description = "0개의 전적을 검색하실 수 없습니다.")
                    isError = True
            
                userName = userName[:-1]
            else:
                countNum = 1

            #전적 검색
            if isError == False:
                for i in range(int(countNum)):
                    tempMsg = await message.channel.send(embed = showLOLUserInfo(userName, i, False if param[1] == "북미" else True))
            else:
                tempMsg = await message.channel.send(embed = msg)
                await asyncio.sleep(10)
                await tempMsg.delete()
    
    #투표
    elif param[0] == "!투표":
        isError = False
        
        #선택지 관련 오류
        if len(param) < 3:
            msg = discord.Embed(title = "!오류", description = "선택지가 2개 이상이어야 합니다.")
            isError = True

        if len(param) > 6:
            msg = discord.Embed(title = "!오류", description = "선택지는 5개를 초과할 수 없습니다.")
            isError = True

        #투표 출력
        if isError:
            msg = await message.channel.send(embed = msg)
        else:
            msg = await message.channel.send(embed = showUserVote(str(message.author), param))
            reaction_list = ["🇦", "🇧", "🇨", "🇩", "🇪"]
            for i in range(len(param) - 1):
                await msg.add_reaction(reaction_list[i])

        await asyncio.sleep(10 if isError else 60)
        await msg.delete()

    #랜덤 선택기
    elif param[0] == "!랜덤":
        await message.channel.send(embed = discord.Embed(title = "태형이의 선택은", description = str(showRandomChoice(param))))

    #주사위
    elif param[0] == "!주사위":
        await message.channel.send(embed = discord.Embed(title = "태형이의 선택은", description = str(random.randrange(int(param[1]), int(param[2])))))
        
    #블서 전적
    elif param[0] == "!블서":
        await message.channel.send(embed = showBSELUserInfo(str(param[1])))

    #수능 D-DAY
    elif param[0] == "!수능":
        await message.channel.send(embed = showSATDDAY())
        
    #명령어 오류
    else:
        msg = await message.channel.send(embed = discord.Embed(title = "!오류", description = "존재하지 않는 명령어입니다"))
        await asyncio.sleep(10)
        await msg.delete()

    if message.content.startswith("!블서"):
        await message.delete()
        param = message.content.split()

        await message.channel.send(embed = showBSELUserInfo(param[1]))

    if message.content.startswith("!여친"):
        await message.delete()
        await message.channel.send(str(message.author) + "님은 여친이 영원히 생기지 않습니다!")

    if message.content.startswith("!남친"):
        await message.delete()
        await message.channel.send(str(message.author) + "님은 저와 영원히 ❤친구❤!")

#봇 명령어 출력
def showServerInfo():
    #임베디드 생성
    embed = discord.Embed(title = "레찐들을 위한 서버 레식하는 찐따들입니다!", description = "====================================", color = 0x000000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/543709358328905730/777064786898190356/Screenshot_20200522-033415.png")
    embed.add_field(name = "!시간 <시간 추가>", value = "현재 캐나다 / 한국 시간을 알려줍니다.", inline = False)
    embed.add_field(name = "!롤 <소환사 이름> <횟수 : 최대 9>", value = "롤 전적을 알려줍니다.", inline = False)
    embed.add_field(name = "!롤 빌드 <챔피언 이름>", value = "롤 챔피언 빌드를 알려줍니다.")
    embed.add_field(name = "!블서 <플레이어 이름>", value = "블랙서바이벌 전적을 알려줍니다.", inline = False)
    embed.add_field(name = "!전장 기물 <등급> <종족>", value ="전장 기물을 알려줍니다.", inline = False)
    embed.add_field(name = "!투표 <선택지 : 최소 2, 최대 5>", value = "투표를 진행할 수 있습니다.", inline = False)
    embed.add_field(name = "!랜덤 <선택지 : 최소 1, 최대 10>", value = "랜덤한 선택지를 골라줍니다.", inline = False)
    embed.add_field(name = "!주사위 <숫자> <숫자>", value = "두 수 사이의 랜덤한 숫자를 골라줍니다.", inline = False)
    return embed

#캐나다 / 한국 시간 출력
def showTime(i):
    #시간 가져오기
    KST = datetime.datetime.now() + datetime.timedelta(hours = 9 + i)
    PST = datetime.datetime.now() - datetime.timedelta(hours = 8 - i)

    #임베디드 생성
    embed = discord.Embed(title = "시간", description = "====================")
    embed.add_field(name = "캐나다 시간", value = str(PST.year) + "년 " + str(PST.month) + "월 " + str(PST.day) + "일 ㅣ" + str(PST.hour).zfill(2) + ":" + str(PST.minute).zfill(2) + ":" + str(PST.second).zfill(2), inline = False)
    embed.add_field(name = "한국 시간", value = str(KST.year) + "년 " + str(KST.month) + "월 " + str(KST.day) + "일 ㅣ" + str(KST.hour).zfill(2) + ":" + str(KST.minute).zfill(2) + ":" + str(KST.second).zfill(2), inline = False)
    return embed

#롤 전적 출력
def showLOLUserInfo(userName, countNum, isNa):
    #주소 설정
    urlServer = "www" if isNa == True else "na"
    source = requests.get("https://" + urlServer + ".op.gg/summoner/userName=" + urllib.parse.quote(userName)).text
    _url = "https://" + urlServer + ".op.gg/summoner/userName=" + str(userName)

    #크롤링 준비
    soup = BeautifulSoup(source, "html.parser")
    gameDatas = soup.select(".GameItemList .GameItemWrap")
    
    #웹에서 정보 가져오기
    game = gameDatas[countNum]
    gameResult = game.select_one(".GameResult").get_text()
    gameTime = game.select_one(".GameLength").get_text()
    gameChampion = game.select_one(".ChampionName a").get_text()
    gameKill = game.select_one(".Kill").get_text()
    gameDeath = game.select_one(".Death").get_text()
    gameAssist = game.select_one(".Assist").get_text()
    gameLevel = game.select_one(".Level").get_text()
    gameCS = game.select_one(".CS .CS").get_text()
    gameKillRate = game.select_one(".CKRate").get_text()

    #임베디드 생성
    embed = discord.Embed(title = userName + "님의 롤 전적", url = _url)
    embed.add_field(name = "---------------------------------------------", value = gameChampion, inline = False)
    embed.add_field(name = "승패", value = gameResult)
    embed.add_field(name = "시간", value = gameTime)
    embed.add_field(name = "KDA", value = gameKill + " / " + gameDeath + " / " + gameAssist)
    embed.add_field(name = "레벨", value = gameLevel.split('l')[1])
    embed.add_field(name = "CS", value = gameCS)
    embed.add_field(name = "킬관여", value = gameKillRate.split(' ')[1])
    embed.set_thumbnail(url = "https://opgg-static.akamaized.net/images/lol/champion/" + gameChampion.replace(" ", "") + ".png")

    return embed

#롤 빌드 출력
def showLOLBuild(ChampionName):
    if LOLCharToEng(ChampionName) == None:
        return discord.Embed(title = "!오류", description = ChampionName + "이라는 챔피언이 존재하지 않습니다.")
    
    #주소 설정
    source = requests.get("https://www.op.gg/champion/" + LOLCharToEng(ChampionName).rstrip("\n") + "/statistics").text

    #크롤링 준비
    soup = BeautifulSoup(source, "html.parser")
    overViewDataList = soup.select(".champion-overview__data")

    #웹에서 정보 가져오기
    GameChamTier = soup.select_one(".champion-stats-header-info__tier > b").get_text().split()[1]
    GameChamSpell = overViewDataList[1]
    #GameChamSkill
    #GameChamStartItem
    #GameChamItemBuild
    #GameChamItemRune

    embed = discord.Embed(title = ChampionName + "의 추천 빌드입니다", url = "https://www.op.gg/champion/" + LOLCharToEng(ChampionName).rstrip("\n") + "/statistics")

    return embed

#롤 챔피언 이름 ( 한글 -> 영어 )
def LOLCharToEng(ChampionName):
    f = open("LOL.txt", 'rt', encoding = "utf-8")
    LOLCharList = f.readlines()

    for i in range(1, 305, 2):
        if LOLCharList[i].rstrip('\n') == ChampionName:
            f.close()
            return LOLCharList[i - 1]
    
    f.close()
    return "챔피언이 존재하지 않습니다"

#투표 임베디드 출력
def showUserVote(userName, param):
    reaction_list = ["🇦", "🇧", "🇨", "🇩", "🇪"]
    embed = discord.Embed(title = userName + "님이 시작하신 투표입니다.", description = "60초 후에 삭제됩니다.")
    for i in range(len(param) - 1):
        embed.add_field(name = reaction_list[i] + "  -  " + param[i + 1], value = "-------------------------------------------------------", inline = False)
    
    return embed

#블서 url 출력
def showBSELUserInfo(userNameData):
    _url = "http://matchhistory.playeternalreturn.com/kr/name=" + urllib.parse.quote(userNameData)

    embed = discord.Embed(title = userNameData + "님의 블서 전적입니다", description = "영원회귀 api 제공전까지는 링크만 제공합니다.", url = _url)

    return embed

#수능 DDAY 생성
def showSATDDAY():
    start_day = datetime.datetime.now() + datetime.timedelta(hours = 9)
    end_day = datetime.datetime.now() + datetime.timedelta(days = 365, hours= 9)

    return discord.Embed(title = "수능까지 " + (end_day - start_day).days + "일 남았습니다.", description = "게임 그만하고 공부하러 가세요.")

def userNameChange(_userName):
    userName = _userName
    userName = userName.replace("!롤", "")
    userName = userName.replace("북미", "")
    userName = userName.replace(" ", "")
    return userName

def showRandomChoice(param):
    randomNum = random.randrange(1, len(param))
    return param[randomNum]

app.run(token)
