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
    code = data.split('A')
    code.pop()
    if data:
        for i in range(len(code)):
            temp = ''
            for с in code[i]:
                temp = temp + str(ord(с)-1040)
            code[i] = temp
        try:
            for i in range(len(code)-2):
                code[i] = chr(int(code[i], int(code[i + 1][-1]) + 2))
            code[len(code)-2] = chr(int(code[len(code)-2], int(code[len(code)-1][-3:], 2) + 2))
            code[len(code)-1] = chr(int(code[len(code)-1], 2))
            code = ''.join(code)
        except IndexError:
            code = "А это и не код"
        except ValueError:
            code = "Это не код или код был поврежден"
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
        code[0] = code[0][2:]
        for i in range(1, len(code)):
            code[i] = base_to_base(code[i], 2, key)
            key = int(code[i][-1]) + 2
        code.reverse()
        for num in code:
            for i in range(len(num)):
                result = result + chr(int(num[i])+1040)
            result += 'A'
    return result


@eel.expose
def copy(data):
    pc.copy(data)


eel.start('index.html', size=(700, 700))



