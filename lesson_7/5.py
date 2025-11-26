'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''

orig_list = ['qwertyu', 'asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for key , val in enumerate(orig_list):
    print(f"{key} - {val} - {val[key]}")