#Есть список интернет-ресурсов. Необходимо получить заголовки всех этих страниц.

import threading
from time import perf_counter

import requests


sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

#without threading

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0
for source in sources:
    start_tmp = perf_counter()
    headers_stor[source] = requests.get(source).headers  # получаем заголовки и формируем словарь
    delta = perf_counter() - start_tmp
    print(source, delta)
    sum_ex_time += delta

print(f"completed in {perf_counter()-start} seconds")  # Считаем общее время выполнения всех запросов
print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(*headers_stor.items(), sep="\n")  # Выводим наши заголовки


#with threading
headers_stor_thr = {}  # Храним здесь заголовки


def get_header(link):
    start_tmp_thr = perf_counter()
    headers_stor_thr[link] = requests.get(source).headers  # получаем заголовки и формируем словарь
    delta_thr = perf_counter() - start_tmp_thr
    print(link, delta_thr)


start_thr = perf_counter()
threads = []

for source in sources:
    threads.append(threading.Thread(target=get_header, args=(source,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"completed in {perf_counter()-start_thr} seconds")  # Считаем общее время выполнения всех запросов
print(*headers_stor_thr.items(), sep="\n")  # Выводим наши заголовки
