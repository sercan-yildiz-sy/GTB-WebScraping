import requests

tex = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/').text
l = []
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

    if tex[i-8:i+1] == '<a href="' and tex[i+1] == 'g':
        for j in range(50):
            if tex[i+j+1] == '"':
                break
            b += tex[i+j+1]
        l.append(b)

ses = []
des = []
for i in l:
    print(i)
    newtex = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/'+i).text
    for i in range(10,len(tex)):
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
    break
print(len(ses))
print(len(des))
    


print(dic['Doğu'])
#print(requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/gazete.php?gazete=aksam').text)
tex = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/gazete.php?gazete=aciksoz').text
#print(tex)
s = []
for i in range(10,len(tex)):
    a = ''
    if tex[i-8:i-1] == '-left">':
        for j in range(50):
            if tex[i+j-1:i+j+2] == '</t':
                break
            a += tex[i+j-1]
        s.append(a)
s.pop()
print(len(s))