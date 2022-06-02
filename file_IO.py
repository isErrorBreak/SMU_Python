# 읽고 쓰기 함수
# 파일 겍체
# 파일로 만들고 저장된다.
import time

def FileTest():
    
    inFile = None
    inList = []
    inString = ""
    time_start = time.time()
    inFile = open('0519.txt','r',encoding='utf8')
    inList = inFile.readlines()

    for inString in inList:
        print(inString, end="")


    inFile.close()
    time_end = time.time()
    return time_start,time_end
FileTest()

def FileTest2():
    outFile = None
    outString = ''
    outFile = open('0519124.pptx','w',encoding='utf8')
    
    while True:
        outString = input("\n메모하세요:")
        
        if outString !="":
            outFile.writelines(outString+"\n")
        else:
            break
    outFile.close()

FileTest2()