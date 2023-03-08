import random
import os

class _word:
    word_num : int = 0
    word_eng : str = ""
    word_meaning : str = ""

    def __init__(self, str):
        self.word_num = int(str[0])
        self.word_eng = str[1]
        self.word_meaning = str[2]

    def _print(self):
        print(self.word_num,self.word_eng,self.word_meaning)



word_list: list[_word] = list()

def init(): 
    word_file : io.TextIOWrapper = open("_data1.txt","r",encoding="UTF-8")

    lines : list[str] = word_file.readlines()
    for line in lines:
        line = line.strip()
        word : list[str] = _word(line.split())
        word_list.append(word)

    word_file.close()

def word_list_print():
    for i in word_list:
        i._print()

init()


_line = "---------------------------------------------------"

def start():
    n = int(input("개수를 입력하세요: "))
    print(_line)
    for i in range(n):
        a = random.randrange(0,10)
        b = random.randrange(0,2)

        if b == 0:
            print("Q:",word_list[a].word_eng)
            tr = input("뜻을 입력하세요: ")
        
            print("A:",word_list[a].word_meaning)
            
            print(_line)
        if b == 1:
            print("Q:",word_list[a].word_meaning)
            tr = input("단어를 입력하세요: ")
            print("A:",word_list[a].word_eng)

            print(_line)


def end():
    print('와 끝났어요')
    os.system('pause')

start()
end()
