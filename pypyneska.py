from tkinter import  *#1
import random
#0) создаем окно
root=Tk()#2
root.title("Виселица")#3
canvas=Canvas(root, width=600, height=600)#6
canvas.pack()#7
#8) Рисуем фонв клеточку
def but():#9 dlya etogo sdelaem otdelnuiu funckiu
    y=0#10 hado opredelyrsya pi X i po Y, t. e. delat poloski, fon - veli, a linii cherni
    while y<600:#11 i ni budem risovat Y do 600
        x=0
        while x<600:#11 i poka x<600
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")#12 nachinaem risovat linii
            x=x+33#13 teper nujno smeshat X i Y v pravilnom napravlenii
        y=y+27#14
#16but()#15 teper vizovem fincksiu chtobi proverit
#17) здороваемся с игроком и объясняем правила, предлагаем начать
faq='''
Privet, davai poigraem.
Princip igri viselca:
Виселица — игра на бумаге для двух человек.'''#18
canvas.create_text(310, 240, text=faq, fill="purple",  font=("Helvetion", "14"))#19 ramestim etot tekst. mi zadaem kodirovannoe polojenie textka
#23) создаем список слов
slova=["виселица", "смартфон", "маргарин", "мегагерц", "страница", "криветка", "микрофон"]#24
#25) В каждом слове выводим на экран только первую и последнюю букву. Остальое заменяем на _
def arr():#26sozdadim otdeluyu funkciu
    but()#65
    word=random.choice(slova)#27 mi doljni vibrat cluchainoe slovo iz nashego spiska
    wo=word[1:-1]#29 nujno vernut vse elementi spiska krome 1go i poslednego
    wor=[]#28 zanesem eot vse v otdelni spisok
    for i in wo:#30 zamenim ostavshiesya bukvi na '_', to est cherez etot scikl, budem vivodit novoe slovo kotoroe budet vivoditsya
        wor.append(i)#31 vudem dobavlyat v nash pustoi spisok po ondoi bukve
    a0=canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetice","18"))#32
    a1= canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a2= canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a3= canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a4= canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a5= canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a6= canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a6= canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetice", "18"))  # 32
#35) Для неизвестных букв создаем список
    list1=[1,2,3,4,5,6]#36
    alfabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюя" #37 spisok vseh vozmojnih bukv, kototie mi budem primeniyat i prinimat otvet
    er=[]#38 sozdadim peremennuiu kotoraya budet otvechat za oshibki
    win=[]#39
    def a(v): #40 sozdadim funkciu kototaya budet dobavlyat bukvi i spiski v ukazannie slova
        ind_alf = alfabet.index(v)#41 teper nujno vibrat bukvu po indeksu kotorya u nas najimaetsya
        key = alfabet[ind_alf]#42
        if v in wor:#43 esli bukva kotoraya mi vveli v hashem slove, i v pustom spiske wor=[] zapisono, to mi doljni vstavit v spisok list[i zamenit], t.e, esli est V v spiske wor
            ind=wor.index(v)#44 to mi doljni dovat s spsok list
            b2=list1[ind]#44
            wor[ind]='1'#45 i zamenyaem
            def kord():#60
                if b2==1:#61
                    x1,y1=315,40#62
                if b2==2:#61
                    x1,y1=347,40#62
                if b2==3:#61
                    x1,y1=380,40#62
                if b2==4:#61
                    x1,y1=412,40#62
                if b2==5:#61
                    x1,y1=444,40#62
                if b2==6:#61
                    x1,y1=477,40#62
                return x1, y1#63
            x1,y1 = kord()#64 zadaem znachenie X i Y
            win.append(v)#57
            a2=canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18"))#58
            btn[key]["bg"]="green"#59 kogda mi ugadivaem, hujno chtob knopki bili zelenimi
            if not v in wor:# 51 teper nujno razmestit sami knopki po X i Y
                btn[key]["stste"]="disabled"#52 to eti knpki budut nahoditsya v vikluchennom sostoiyani
            if v in wor:
                win.append(v)#53 togda nado budet dobavit v spisok
                ind2=wor.index(v)#54 dobavl index
                b2=list1[ind2]#55 dobavit eshe spisok
                x1,y1=kord()#75
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))#76
            if len(win)==6:#77esli dlina budet = 6
                canvas.create_text(150, 150, text="Ti pobedil", fill="purple", font=("Helvetica", "18"))#56 i napisat text
                #69) проверяем правильность ответов
                for i in alfabet:#70 sdelaem tak chto bi knopki snova stali ne najatie
                    btn[i]["state"]="disabled"#71
        else:#72
            er.append(v)#73
            btn[key]["bg"]="red"#74
            btn[key]["state"]="disabled"#75sdelaem etu knopku ne aktivnoi
            if len(er)==1:#81 esli odna oshibka, to mi dlojni risovat krug
                golova()
            elif len(er)==2:#82
                telo()
            elif len(er)==3:#83
                rukaP()
            elif len(er)==4:#84
                rukaL()
            elif len(er)==5:  # 85
                nogaL()
            elif len(er)==6:  # 86
                nogaP()
                end()#87
            root.update()#91
    # 46) создаем кнопки с буквами
    btn={}
    def gen(u, x, y):#47 teper sdelaem sami knopki, dlya etogo mi propishem otdelnuiu funkciu i peredaem znacheniu po X i Y, i znachenie pravilnost na ne pravilnost
        #49btn[u]=Button(root, text=u, width=3, height=1)#47 sozdal knopku
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))  #50 teper kogda mi najali na knopku, mi doljni vizivat funcksiu a(v)
        btn[u].place(x=str(x), y=str(y))#48 i postavim eto knopku
    x=265# 66postvim teper bukvi
    y=110
    for i in alfabet[0:8]:#67
        gen(i, x, y)#68vizivaem nashu funckii gen, rameshaem knopku v pravilnom X i Y
        x=x+33#69 smeshaem kajduiu bukvu po X na 33 px
    x=265
    y=137
    for i in alfabet[8:16]:
        gen(i, x, y)
        x=x+33
    x=265
    y=164
    for i in alfabet[16:24]:
        gen(i, x, y)
        x=x+33
    x=265
    y=191
    for i in alfabet[24:33]:
        gen(i, x, y)
        x=x+33#70doljno bilo poayvitsya bukvi iz 4k strok
    # 9) рисуем части туловища
    def golova():#88
        canvas.create_oval(79, 59, 120, 80, width=4, fill='grey')#89
        root.update()#90
    def telo():
        canvas.create_line(100, 80, 100, 200, width=4)
        root.update()
    def rukaP():
        canvas.create_line(100, 80, 145, 100, width=4)
        root.update()
    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4)
        root.update()
    def nogaL():
        canvas.create_line(100, 200, 45, 300, width=4)
        root.update()
    def nogaP():
        canvas.create_line(100, 200, 145, 300, width=4)
        root.update()
    def end():#77
        canvas.create_text(150, 150, text="ti priogral",  fill="purple", font=("Helvetica", "18"))#78
        for i in alfabet:#79
            btn[i]["state"]="disabled"#80
#33 btn01=Button(root, text="Haachat", width=10, height=2)#20 sozdadim knopku dlya predlojenya ogroku igrat
btn01 = Button(root, text="Haachat", width=10, height=1, command=lambda: arr())  #34 pri najatii na knopku nachat, mi vizivali eit slova
btn01.place(x=250, y=542)#21 raspolojim etu knopku v X i Y po centru
btn01["bg"]="red"#22 sdelaen knopku krasivoi
root.mainloop()#4
