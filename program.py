# -*- coding: utf-8 -*-

def outsymbol (i):#Функция возвращает символ на позиции i из алфавита.
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАаБбВвГгДдЕеꄍꄎЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя瀕瀖瀗瀘瀙瀚瀛瀜瀝瀞瀟瀠瀡瀢瀣瀤瀥瀦瀧瀨瀩瀪瀫瀬瀭瀮瀯瀰瀱瀲瀳瀴瀵瀶瀷瀸瀹瀺瀻瀼瀽瀾瀿灀灁灂灃灄灅灆灇灈灉灊灋灌灍灎灏灐灑灒灓灔灕灖灗灘灙灚灛灜灝灞灟灠灡灢灣灤灥灦灧灨灩灪火灬灭灮灯灰灱灲灳灴灵灶灷灸灹灺灻灼災灾灿炀炁炂炃炄炅炆炇炈炉炊炋炌炍炎炏炐炑炒炓炔'
    return (alphabet[i])

def insimvol(i):#Функция возвращает позицию i из алфавита.
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАаБбВвГгДдЕеꄍꄎЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя瀕瀖瀗瀘瀙瀚瀛瀜瀝瀞瀟瀠瀡瀢瀣瀤瀥瀦瀧瀨瀩瀪瀫瀬瀭瀮瀯瀰瀱瀲瀳瀴瀵瀶瀷瀸瀹瀺瀻瀼瀽瀾瀿灀灁灂灃灄灅灆灇灈灉灊灋灌灍灎灏灐灑灒灓灔灕灖灗灘灙灚灛灜灝灞灟灠灡灢灣灤灥灦灧灨灩灪火灬灭灮灯灰灱灲灳灴灵灶灷灸灹灺灻灼災灾灿炀炁炂炃炄炅炆炇炈炉炊炋炌炍炎炏炐炑炒炓炔'
    return (alphabet.find(i))

def byte_file(seek,number,way):#Функция возвращает байт файла way на позиции i.Первый байт равен 0,последний равен размеру.ПЕРЕДЕЛАТЬ.
    file = open(way,"rb")
    file.seek (seek)
    return (file.read(number))
    file.close

def razmer(size):#Функция возвращает main(главные папки(количество)) и a*255+i(внутренние папки(количество)).Полезно для создания счетчика прогресса.
    a = size // 32640
    residue = size % 32640
    maxname = 255
    size = 1
    if residue == 0:
        size = 0
    else:
        while residue >= maxname:
            residue = residue - maxname
            maxname = maxname-1
            size += 1
    if residue > 0:
         main = a+1
    return(main,a*255+size)

def lsyandex(path):#Функция возвращает внутренности папки path(unix-way:ls).
    yavi=str(webdav.ls(path))
    a = []
    while yavi.find('name')>-1:
        a.append(urllib.request.unquote(yavi[yavi.find('name')+6:yavi.find("', size")]))#Вырезка
        yavi=yavi[yavi.find("', size")+4:]#Смещение на новый участок регулярного выражения.
    a.sort(key=len)
    size=len(a[0])
    a.pop(0)
    for z in range(len(a)-1,-1,-1):
        a[z]=a[z][size:-1]
    return(a)

def sha1OfFile(filepath):#Функция возвращает sha1(хеш) файла
    import hashlib
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def short_name(filepath):#Функция возвращает имя файла(добавить различные слеши).
    simvol=r"D\D"
    return (filepath[filepath.rfind(simvol[1])+1:])

def mkdirglav (nomerpapok):
    webdav.mkdir(mainfolder+'/'+name+'/'+str(nomerpapok))

def mkdirvspom (s) :
    webdav.mkdir(mainfolder+'/'+name+'/'+str(directory)+'/'+str(s))
            
def filezal(i,papoh):
    tt=str(i)
    name=papoh+tt
    file=open(name, "wb")
    a=lsyandex(link+str(i)+'/')
    for z in range(len(a)-1,-1,-1):#Цикл по файлам
        stroka=a[z]
        for g in range(0,len(stroka)):#Цикл по буквам
            file.write(bytes([int(insimvol(stroka[g]))]))

def popitka(popi):
        webdav.mkdir(popi)


        
import easywebdav
import os
import urllib
import sys
import time
import threading
import shutil
from futures import ThreadPoolExecutor, as_completed

#Получение логина и пароля
login = input("Логин (пример:proba@yandex.ru) : ")
password =   input("Пароль : ")

#Активные потоки
maxconnect= int(input("Количество активных потоков : "))

#Переменные для многопоточности
threads = []
shit=0
shitproverka=0
maxconnecttwo=25


#Выбор скачивания или загрузки
l_d = int(input('0-Загрузка файла на сервер Яндекса;1-Скачивание файла с сервера Яндекса : '))

webdav = easywebdav.connect('webdav.yandex.ru', username=login, password=password,protocol='https')

#Ветка загрузки
if  l_d == 0:
    
    file = str(input('Путь к загружаемому файлу : '))
    if True != os.path.exists(file):
        print ('Такого файла не существует.')
        sys.exit()
        
    mainfolder = str(input('Название главной папки : '))
    start = time.time()
    
    #Форматирование линка
    if  mainfolder[len(mainfolder)-1:] == '/':
        mainfolder=mainfolder[0:len(mainfolder)-1]

    size=os.path.getsize(file)
    glav,vspom=razmer(size)
    name=short_name(file)+'('+str(size)+';'+sha1OfFile(file)+')'
    maxname = 255
    i = maxname
    directory = 1
    k = 0
    s = ''
    list=[]
    process=0
    proidennoe=0
    massiv=[]
    ruk=0
    #poolvspom = ThreadPoolExecutor(max_workers=maxconnect)
    
    #Проверка корня
    try:
        webdav.mkdir(mainfolder)
    except easywebdav.client.OperationFailed:
        print ('Корень существует.Продолжаем.')
        
    #Проверка аналогичного файла
    try:
        webdav.mkdir(mainfolder+'/'+name)
    except easywebdav.client.OperationFailed:
        print('Папка существует.Поменяйте имя файла на другое.')
        sys.exit()

    #Скрипт загрузки
    #Создание главных папок
        
    print ('Создание главных папок.')

    with ThreadPoolExecutor(max_workers = maxconnect) as poolglav:
        results = [poolglav.submit(mkdirglav, nomerpapok) for nomerpapok in range(1,glav+1)]

    #Создание внутренних папок(костыль,позже реализовать через пул)

    print ('Создание внутренних папок.')

    if size > maxname:
        for a in range(0,vspom-1):
            for dlinaimeni in range (0,i):
                list.append(outsymbol(byte_file(proidennoe+dlinaimeni,1,file)[0]))
            s = "".join([str(list[uli]) for uli in range(len(list))])
            #poolvspom.submit(mkdirvspom,s)
            #poolvspom.shutdown
            pot=threading.Thread(target=mkdirvspom,args=[s])
            threads.append(pot)
            pot.start()
            shit += 1
            if shit > maxconnect:
                for pot in threads:
                    pot.join()
                shit=0
            print(str(a+1)+'/'+str(vspom))
            s = ''
            list=[]
            proidennoe=proidennoe+i
            if i>1 :
                i -= 1
            else :
                directory += 1
                i = maxname

    for dlinaimeni in range (0,size-proidennoe):
        list.append(outsymbol(byte_file(proidennoe+dlinaimeni,1,file)[0]))
    s = "".join([str(list[uli]) for uli in range(len(list))])
    pot=threading.Thread(target=mkdirvspom,args=[s])
    threads.append(pot)
    pot.start()
    #poolvspom.submit(mkdirvspom,s)
    print(str(a+2)+'/'+str(vspom))
    #poolvspom.shutdown

    for pot in threads:
        pot.join()
        
    print ('Загрузка выполнена.')
        
    #Затраченное время
    finish = time.time()
    print ('Затраченное время в секундах:'+str(int(round(finish - start))))
            
#Ветка скачивания   
elif l_d==1:
    
    fileout=str(input(r'Путь сохранения файла с его названием (пример: C:\file.txt ): '))
    papoh=str(input(r'Путь для сохранения временных файлов (пример: C:\file ): '))

    #Проверка существования файла
    if os.path.exists(fileout) == False:
        file=open(fileout,'wb')
    else :
        print ('Файл с таким именем уже существует.')
        sys.exit()
        
    link=str(input('Введите ссылку на скачиваемый файл : '))

    #Форматирование линка
    if  link[len(link)-1:] != '/':
        link=link+'/'

    #Вычисление необходимых данных
    size=int(link[link.find('(')+1:link.find(';')])#Вырезка
    c,b=razmer(size)
    
    #Скачивание(допилить в многопоточность)
    print ('Скачивание.')

    simvol=r"D\D"
    os.mkdir(papoh)
    if  papoh[len(papoh)-1:] != simvol[1]:
        papoh=papoh+simvol[1]

    for i in range(1,c+1):#Цикл по папкам
        pot=threading.Thread(target=filezal,args=[i,papoh])
        threads.append(pot)
        pot.start()
        shit += 1
        print(str(i)+'/'+str(c))
        if shit > maxconnect:
            for pot in threads:
                pot.join()
            shit=0
            time.sleep(5)

    for pot in threads:
        pot.join()

    #Склейка файлов
    print ('Склейка файлов.')
    for i in range(1,c+1):
        name=papoh+str(i)
        filein=open(name,"rb")
        file.write(filein.read(os.path.getsize(name)))
    file.close()

    #print ('Удаление папки.')
    #for i in range(1,c+1):
        #name=papoh+str(i)
        #os.remove(name)
    #os.rmdir(papoh)

    print('Скачивание завершено.')

    #Проверка хеша
    print ('Подсчёт хеша.')
    if sha1OfFile(fileout) == link[link.find(';')+1:link.find(')')]:#Вырезка
        print ('Хеш совпадает.')
    else : print ('Хеш не совпадает.')
    
else:
    print('0-Загрузка файла на сервер Яндекса;1-Скачивание файла с сервера Яндекса.')
