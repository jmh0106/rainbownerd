# 파일 임포트
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# 권한 불러오기
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
sheetAuth = gspread.authorize(credentials)

# 파일 열기
sheetNote = sheetAuth.open("RainbowNerdData").worksheet('메모')
sheetNoteValue = sheetNote.get_all_values()

def printNote():
    for i in sheetNoteValue:
        print(i[0] + i[1])

def writeNote(userName, noteDes):
    sheetNoteValue = sheetNote.get_all_values()
    writeNum = str(len(sheetNoteValue) + 1)
    sheetNote.update_acell("A" + writeNum, userName)
    sheetNote.update_acell("B" + writeNum, noteDes)
    sheetNoteValue = sheetNote.get_all_values()

def deleteNote(userName, noteNum):
    sheetNoteValue = sheetNote.get_all_values()
    if (userName == sheetNoteValue[noteNum - 1][0]):
        for i in range(noteNum, len(sheetNoteValue)):
            sheetNote.update("A" + str(i), sheetNoteValue[i][0])
            sheetNote.update("B" + str(i), sheetNoteValue[i][1])
        sheetNote.update("A" + str(len(sheetNoteValue)), '')
        sheetNote.update("B" + str(len(sheetNoteValue)), '')
        sheetNoteValue = sheetNote.get_all_values()