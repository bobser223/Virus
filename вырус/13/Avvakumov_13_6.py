#Описати підпрограму, яка за заданою послідовністю символів формує текстовий
# файл із рядками по 40 літер (в останньому рядку літер може бути й менше).

text = "aaaaaaaaaaaaaaaaaavsgdcvgsdhabregfarebhfbhabhjhjavbhjfdbahaffhguiaerhuiarehhdghahkfhauiforegfb"

def prnt(a:list):
    f = open("file_13_6", "wt")
    i = 0
    ii = 40
    for iii in range((len(text) // 40)+1):
        print(a[i:ii], file=f)
        i += 40
        ii += 40
    f.close()
prnt(text)