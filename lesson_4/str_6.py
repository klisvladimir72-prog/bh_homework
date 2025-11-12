"""
Дана строка - "Это тестовая <start>строка для изучения<end> строковых операций".
Программа должна вывести на экран текст из данной строки
заключенный между тэгами <start> и <end>.
Программа должна работать с любой другой строкой с подобными тэгами.

"""

string_search = "Программа должна вывести на экран текст из данной строки заключенный между тэгами <start> и <end>."

start_index = "<start>"
end_index = "<end>"

start_string = string_search.find(start_index) + len(start_index)
end_string = string_search.find(end_index)


print(string_search[start_string:end_string].strip())
