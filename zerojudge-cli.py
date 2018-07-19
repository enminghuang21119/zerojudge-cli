import requests
from bs4 import BeautifulSoup
import colorTable as cT
headers={}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
loginurl='https://zerojudge.tw/Login'
logouturl='https://zerojudge.tw/Logout'
Userurl='https://zerojudge.tw/UserStatistic'
resurl='https://zerojudge.tw/Submissions'
user={'token':''}
purl='https://zerojudge.tw/Solution.api?action=SubmitCode&'
session=requests.session()
account=''
def Login():
    account=input('accout:')
    pswd=input('password:')
    user['account']=account
    user['passwd']=pswd
    session.post(loginurl,user,headers=headers)
    if dashBoard(1)==1:
        return 1
    return 0
def submitCode():
    data={}
    problem=input('Problem:')
    lang=input('language(Default is CPP):')
    if lang=='':
        lang='CPP'
    data['language']=lang
    codes=[]
    print('Code:')
    while True:
        code=input() 
        if code:
            codes.append(code)
        else:
            break
    data['code']='\n'.join(codes)
    data['problemid']=problem
    data['contestid']=0
    session.post(purl,data=data,headers=headers)
def Help():
    print('Type dashboard or d to see the dashboard') 
    print('Type s or submit to submit code')
    print('Type h for help')
    print('Type quit or exit to logout and quit')
def dashBoard(flag):
    soup=BeautifulSoup(session.get(resurl,headers=headers).text,"html5lib")
    if len(soup.find_all('tr',attrs={'solutionid':True}))==0:
        return 1
    if flag:
        return 0
    cnt=0
    for i in soup.find_all('tr',attrs={'solutionid':True}):
        if cnt==5:
            break
        solveId=i.find('td',id='solutionid').text
        userId=[]
        userId.append(i.find('a',attrs={'title':True}).text)
        userId.append(i.find('span',attrs={'title':True}).text)
        pr=[]
        p=i.find_all('a',attrs={'title':True})[1]
        pr.append(p.get('href').split('=')[1])
        pr.append(p.text)
        resp=[]
        resp.append(i.find('span',id='judgement',attrs={'data-solutionid':solveId}).text)
        resp.append(i.find_all('span',id='summary')[1].text)
        print(solveId,userId[0],userId[1],pr[0],pr[1])
        print(cT.bcolors.BOLD)
        str1=''.join(list(filter(str.isalnum,resp[0])))
        if str1=='AC':
            print(cT.bcolors.OKGREEN+str1)
        elif str1=='TLE':
            print(cT.bcolors.OKBLUE+str1)
        else:
            print(cT.bcolors.WARNING+str1)
        print(cT.bcolors.ENDC,resp[1])
        cnt=cnt+1
    return 0
while Login()==1:
    print('Login failed ,try again')
while True:
    c=input(cT.bcolors.OKBLUE+cT.bcolors.BOLD+'>>'+cT.bcolors.ENDC) 
    if c=='h':
        Help()
    elif c=='submit' or c=='s':
        submitCode()
    elif c=='dashBoard' or c=='d':
        dashBoard(None)
    elif c=='quit' or c=='exit': 
        break 
    else:
        print('Unknown command , type h for help')
        continue
session.get(logouturl,headers=headers)
