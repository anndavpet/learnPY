morze = {".-": "А", "-...": "Б", ".--": "В", "--.": "Г",
         "-..": "Д", ".": "Е", "...-": "Ж", "--..": "З",
         "..": "И", ".---": "Й", "-.-": "К", ".-..": "Л",
         "--": "М", "-.": "Н", "---": "О", ".--.": "П",
         ".-.": "Р", "...": "С", "-": "Т", "..-": "У",
         "..-.": "Ф", "....": "Х", "-.-.": "Ц", "---.": "Ч",
         "----": "Ш", "--.-": "Щ", ".--.-": "Ъ", "-.--": "Ы",
         "-..-": "Ь", "...-...": "Э", "..--": "Ю", ".-.-": "Я",
         "-...-": " "}

lst = []

s = input().split()

for i in range(len(s)):
    lst.append(morze[s[i]].lower())

print(''.join(lst))