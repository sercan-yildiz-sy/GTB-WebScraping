import requests
# This script scrapes the Istanbul University Newspaper Archive and saves dates and URLs of newspapers in a JSON file.
main_page = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/').text
urlList = []
newsPaperList = []
newsPaperDict = {}

#The main page is parsed to find newspaper names and their URLs.
for i in range(5,len(main_page)):
    newsPaperName = ''
    newsPaperUrl = ''

    # The newspaper names are identified by the pattern 'd-block">'
    if main_page[i-8:i+1] == 'd-block">':
        for j in range(50):
            if main_page[i+j+1] == '<':
                break
            newsPaperName += main_page[i+j+1]
        newsPaperDict[newsPaperName] = []
        newsPaperList.append(newsPaperName)
    
    # The URLs are identified by the pattern '<a href="g'.
    if main_page[i-8:i+1] == '<a href="' and main_page[i+1] == 'g':
        for j in range(50):
            if main_page[i+j+1] == '"':
                break
            newsPaperUrl += main_page[i+j+1]
        urlList.append(newsPaperUrl)

# The script iterates through the list of newspapers and scrapes each newspaper's page for dates and URLs.
for k in range(len(newsPaperList)):
    newspaperEach = urlList[k]
    datesList = []
    urlsList = []
    newpaperPage = requests.get('https://nek.istanbul.edu.tr/ekos/GAZETE/' + newspaperEach).text
    
    # 
    for i in range(10,len(newpaperPage)):    
        # The dates are identified by the pattern '-left">'
        eachDate = ''
        if newpaperPage[i-8:i-1] == '-left">':
            for j in range(50):
                if newpaperPage[i+j-1:i+j+2] == '</t':
                    break
                eachDate += newpaperPage[i+j-1]
            datesList.append(eachDate)
        
        # The URLs are identified by the pattern 'href="'
        eachUrl = ""
        if newpaperPage[i-7:i-1] == 'href="':
            for j in range(150):
                    if newpaperPage[i+j-1] == '"':
                        break
                    eachUrl += newpaperPage[i+j-1]
            urlsList.append(eachUrl)
    # The last entry in datesList and the first 18 entries in urlsList are removed, and the last 8 entries in urlsList are also removed as they are not relevant.
    datesList.pop()
    urlsList = urlsList[18:-8]

    # The dates and URLs are combined into a list of tuples and added to the dictionary with the newspaper name as the key.
    newsPaperDict[newsPaperList[k]] = list(zip(datesList, urlsList))
    


import json

# The results are saved in a JSON file named 'newspapers.json'.
with open('newspapers.json', 'w', encoding='utf-8') as f:
    json.dump(newsPaperDict, f, ensure_ascii=False, indent=2)
