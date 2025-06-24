import requests

tex = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/').text
l = []
s = []
dic = {}
#print(tex)
for i in range(5,len(tex)):
    a = ''
    b = ''
    if tex[i-8:i+1] == 'd-block">':
        for j in range(50):
            if tex[i+j+1] == '<':
                break
            a += tex[i+j+1]
        dic[a] = []
        s.append(a)
    if tex[i-8:i+1] == '<a href="' and tex[i+1] == 'g':
        for j in range(50):
            if tex[i+j+1] == '"':
                break
            b += tex[i+j+1]
        l.append(b)
for ss in range(len(l)):
    b = l[ss]
    print(b)
    ses = []
    des = []
    newtex = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/'+b).text
    for i in range(10,len(newtex)):
        a = ''
        if newtex[i-8:i-1] == '-left">':
            for j in range(50):
                if newtex[i+j-1:i+j+2] == '</t':
                    break
                a += newtex[i+j-1]
            ses.append(a)
        b = ""
        if newtex[i-7:i-1] == 'href="':
            for j in range(150):
                    if newtex[i+j-1] == '"':
                        break
                    b += newtex[i+j-1]
            des.append(b)
    ses.pop()
    des = des[18:-8]
    print(len(ses), len(des))
    dic[s[ss]] = [ses, des]


print(dic['Yeni Asır'][0][5],dic['Yeni Asır'][1][5])

import json


with open('newspapers.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)

    #beyoglu, en son dakika, haber, son posta, son saat, 

    #ulus sesi, ulusal birlik, birbirinin sayisini aldi