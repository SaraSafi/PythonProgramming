morsecode={ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}
CODE_REVERSE= {value:key for key,value in morsecode.items()}
def to_morse(text):
    morse=''
    for i in text:
        if i==' ':
            morse+='     '
        else:
            morse+=morsecode[i]+" "
    return morse
text=input('text:').upper()
print(to_morse(text))

def to_text(morse):
    text=''
    for i in morse.split():
        if i!='':
            text+=CODE_REVERSE[i]+''
        else:
            text +=''
    return text.lower()
morse=input('morse:')
print(to_text(morse))

