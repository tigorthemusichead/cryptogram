import eel
import pyperclip as pc

eel.init('front')


def base_to_base(number: str, base_gotten: int, base_given: int):
    dec = int(number, base_gotten)
    result = ''
    while dec > 0:
        result = str(dec % base_given) + result
        dec //= base_given
    return result


@eel.expose
def translate_from(data):
    code = data.split('_')
    code.pop()
    if data:
        for i in range(len(code)):
            temp = ''
            for с in code[i]:
                temp = temp + str(ord(с)-200)
            code[i] = temp
        for i in range(len(code)-1):
            if len(code) - i == 2:
                code[i] = chr(int(base_to_base(code[i], int(code[i + 1][-3:]) + 2, 2)))
            else:
                code[i] = chr(int(base_to_base(code[i], int(code[i+1][-1])+2, 2)))
        print(1)
    return code


@eel.expose
def translate_to(data):
    code = []
    result = ''
    if data:
        for с in data:
            code.append(int(ord(с)))
        code = list(map(bin, code))  # перевод в двоичную систему
        code.reverse()
        key = int(code[0][-3:], 2) + 2   # основание системы счисления предпоследнего числа
        code[0] = code[0][3:]
        for i in range(1, len(code)):
            code[i] = base_to_base(code[i], 2, key)
            key = int(code[i][-1]) + 2
        code.reverse()
        for num in code:
            num = '0'*(len(num) % 3) + num
            for i in range(0, len(num), 3):
                result = result + chr(int(num[i:i+3])+200)
            result += '_'
    return result


@eel.expose
def copy(data):
    pc.copy(data)


eel.start('index.html', size=(700, 700))
