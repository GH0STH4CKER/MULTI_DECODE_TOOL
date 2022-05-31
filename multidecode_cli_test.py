import os,codext
from colorama import init,Fore
init()
def encodeSTR(inputStr):

    for i in codext.list_encodings():
        try:
            a = codext.encode(inputStr,encoding=i)
        except Exception as e:
            pass
        else:
            print('\x1b[92m'+i,'Decoded : ',a)
def decodeSTR(inputStr):

    for i in codext.list_encodings():
        try:
            a = codext.decode(inputStr,encoding=i)
        except Exception as e:
            pass
        else:
            print('\x1b[92m'+i,'Decoded : ',a)
def clearOutput():
    if os.name == 'nt' :
        os.system('cls')
    else :
        os.system('clear')

banner="""████████████████████████████████████████████████████████████████████
█▄─▀█▀─▄█▄─██─▄█▄─▄███─▄─▄─█▀░██▀▀▀▀▀██▄─▄▄▀█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─█
██─█▄█─███─██─███─██▀███─████░██████████─██─█─███▀█─██─██─██─██─▄█▀█
▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀
\x1b[93m--------------------------------------------------------------------
    [#] Coded by GH0STH4CK3R   |     [i] Encode/Decode Anything 
--------------------------------------------------------------------
"""
print('\x1b[92m'+banner)
choice = int(input("""  [1] Encode Text  
  [2] Decode text\n
Choose > """))
if choice == 1 :
    inputStr = input("Enter text to encode > ")
    encodeSTR(inputStr)
    
elif choice == 2 :
    inputStr = input("Enter text to decode > ")
    decodeSTR(inputStr)
else :
    print('\x1b[91m'+'[X] Invalid Choice')

def encodeSTR(inputStr):

    for i in codext.list_encodings():
        try:
            a = codext.encode(inputStr,encoding=i)
        except Exception as e:
            pass
        else:
            print('\x1b[92m'+i,'Decoded : ',a)

def decodeSTR(inputStr):

    for i in codext.list_encodings():
        try:
            a = codext.decode(inputStr,encoding=i)
        except Exception as e:
            pass
        else:
            print('\x1b[92m'+i,'Decoded : ',a)

if input("\nRun Again [y/n] > ").lower() == "y":
    clearOutput()
    import multidecode_cli_test
else :
    exit()
