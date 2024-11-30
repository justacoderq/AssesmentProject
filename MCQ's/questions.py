from questionBank import *
import random
import time
import pickle

#Number of questions
def project():
    totalQuestions=len(ques)
    n=int(input('Enter No. of Questions to generate out of {}:'.format(totalQuestions)))

    if n>totalQuestions:
        print('Sorry !!! :( ')
    else:
        testQuestions=[]
        i=1
        points=1
        score=0
        while i<=n:
            ans=None
            x=random.randint(1,totalQuestions)
            if x not in testQuestions:
                testQuestions.append(x)
                print("%-5s"%(i),end='')
                print(ques[x]['question'])
                print("%-5s%-35s%-5s%-35s"%('a)',ques[x]['a'],'b)',ques[x]['b']))
                print("%-5s%-35s%-5s%-35s"%('c)',ques[x]['c'],'d)',ques[x]['d']))
                ans=input('Enter your correct option: ').lower()
                print('Checking answer... Please wait!!!')
                time.sleep(0.25)
                try:
                    if ques[x][ans] == ques[x]['ans']:
                        print('Well Done... Correct Answer!!!')
                        score+=points
                    else:
                        print('WRONG ANSWER')
                        print('You said: ',ques[x][ans],end='\t')
                        print('But it is: ',ques[x]['ans'])
                    
                    print()
                    i=i+1
                except:
                    print('Wrong input & Now Question Changed\n\n\n')
                    
        print('\nYou scored ',score,'out of',n*points)


def dumpToBinaryFile():
    fw = open('myQuestions.dat','ab')
    for q in ques:
        pickle.dump(ques[q],fw)
    fw.close()
    print("Question saved in data file.")

def getSubjects():
    sub=[]
    fr = open('myQuestions.dat','rb')
    try:
        while fr:
            ques=pickle.load(fr)
            if ques['sub'] not in sub:
                sub.append(ques['sub'])
    except:
        fr.close()
    return sub

def getQuestions(sub):
    sub_ques=[]
    fr = open('myQuestions.dat','rb')
    try:
        while fr:
            ques=pickle.load(fr)
            if ques['sub'] == sub:
                sub_ques.append(ques)
    except:
        fr.close()
    return sub_ques


def mainMenu():
    print("0. Exit")
    print("1. Admin Login (Inactive)")
    print("2. User Login (Inactive)")
    print("3. Read the Questions: ")
    ch = int(input("Enter Your Choice: "))
    if ch==0:
        print("Bye!!!")
    elif ch==3:
        sub=getSubjects()
        sub=input(f"Select the subject{sub}: ")
        

