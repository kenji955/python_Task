nameList=["たんじろう","ぎゆう","ねずこ","むざん"]

def nameCheck(checkName):
    for name in nameList:
        if name == checkName:
            print(checkName+'は含まれます')

testName = 'ぎゆう'

nameCheck(testName)