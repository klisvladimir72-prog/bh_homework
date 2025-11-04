"""
Дана строка - "Это тестовая <start>строка для изучения<end> строковых операций".
Программа должна вывести на экран текст из данной строки
заключенный между тэгами <start> и <end>.
Программа должна работать с любой другой строкой с подобными тэгами.

"""

stringSearch = "Программа должна вывести на экран текст из данной строки заключенный между тэгами <start> и <end>."

startIndex = "<start>"
endIndex = "<end>"

startString = stringSearch.find(startIndex) + len(startIndex)
endString = stringSearch.find(endIndex)


print(stringSearch[startString:endString].strip())
