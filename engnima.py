import csv
import random
import os




def csvin(filename):
  wordbox = []

  with open(filename,'r') as f:
    reader = csv.reader(f)
    wbox = list(reader)
  
  for w in wbox:
    if len(w) != 0:
      wordbox.append(w)  
  
  return wordbox  
  
  
  
  
def statistics(wbox):

  abc = []
  tmp = ''
  sum = 0

  print(logo)
  
  for j in wbox:
    tmp += j[0][0]
    if j[0][0] not in abc:
      abc.append(j[0][0])  

  for i in abc:
    print(logo,i,tmp.count(i))
    sum += tmp.count(i)
  
  print(logo,'Total words:',sum)      
  
  

  
def teacher(data):
  rice = '*'*(len(data[0])-2)
  test = '%s%s%s'%(data[0][0], rice, data[0][-1])
  wrong = False
  print(logo,test,data[1])
  while True:
    ans = input(logo+' ').lower()
    if ans == data[0]:
      print(logo,'correct!!!')
      print(logo)
      break
    else:  
      wrong = True
      print(logo,data[0])
   
  return wrong
  
  
  
  
def welcome():
  print('\n'*2)
  print('='*37+'Engnima'+'='*36)
  print('='*22+'english_7000_vocabularies_exam_system'+'='*21)  
  print('='*31+'powered_by_c0xffee'+'='*31)
  print('\n'*5)
  
  

  
def mark():
  c0xffee = '''

  
  
  

    :'######::::'#####:::'##::::'##:'########:'########:'########:'########:
    '##... ##::'##.. ##::. ##::'##:: ##.....:: ##.....:: ##.....:: ##.....::
     ##:::..::'##:::: ##::. ##'##::: ##::::::: ##::::::: ##::::::: ##:::::::
     ##::::::: ##:::: ##:::. ###:::: ######::: ######::: ######::: ######:::
     ##::::::: ##:::: ##::: ## ##::: ##...:::: ##...:::: ##...:::: ##...::::
     ##::: ##:. ##:: ##::: ##:. ##:: ##::::::: ##::::::: ##::::::: ##:::::::
    . ######:::. #####::: ##:::. ##: ##::::::: ##::::::: ########: ########:
    :......:::::.....::::..:::::..::..::::::::..::::::::........::........::
	
'''
  
  
  engnima = '''
              _______ __   _  ______ __   _ _____ _______ _______
              |______ | \  | |  ____ | \  |   |   |  |  | |_____|
              |______ |  \_| |_____| |  \_| __|__ |  |  | |     |
                                                                 
																 
																 
''' 
  
  
  print(c0xffee)
  print(engnima)
  
  

  
def help():
  print(logo)
  print(logo,'Engnima a english vocabularies exam system,')  
  print(logo,'which can make you remember lots of vocabularies in a short time')
  print(logo)
  print(logo,'p0wered_by_c0xffee')
  print(logo)
  print(logo)
  print(logo,'Command:')
  print(logo,'  help, -h, ?      show help table')
  print(logo,'  stat             print the first alphabet\'s frequency statistic')
  print(logo,'  exit()           exit Engnima')
  print(logo,'  vocabulary       show the word\'s meaning in 7000 words\' list')
  print(logo,'  quiz             take a eazy quiz with random vocabularies')
  print(logo,'  exam             take a exam for diff level')
  print(logo,'\t')
  
  
  
  
def exit():
  print(logo,'Engnima_closed')  
  
  
  
  
def quiz(wordbox):
  times = -1

  while True:
    print(logo)
    print(logo,'<QUIZ>')
    times = int(input('%s wh@t_number_of_word$_do_u_w@nt_2_te$t?? : '%logo)) 
    print(logo)
    print(logo)
    if times < 0 or times > len(wordbox):
      print(logo,'err0r: input must >= 0 and <= ',len(wordbox))
    else:
      break    
      
  tmp = []
  while len(tmp) < times:
    idx = random.randint(0,len(wordbox))
    tmp.append(wordbox[idx])
  wnum = 0  
  for data in tmp:
    wnum += teacher(data)
  print(logo)
  if times == 0:
    print(logo,'correct%:',0.0,'%')
  else:
    print(logo,'correct%:',(1-wnum/times)*100,'%')
  print(logo,times-wnum,'/',times)
  ##statistics()
  

  
  


def exam(wbox,level):

  print(logo)
  print(logo,'<EXAM>')
  ##level = int(input('%s '%logo))
  num = 20
  
  wrongbox = []
  exbox = []
  for i in range(num):
    exbox.append(wbox[i+(level-1)*num])
  
  
  for i in xrand(num):
    if teacher(exbox[i]):
      wrongbox.append(exbox[i])
  
  
  
  while len(wrongbox) > 0:
    i = random.randint(0,len(wrongbox)-1)
    if not teacher(wrongbox[i]):
      del wrongbox[wrongbox.index(wrongbox[i])]
  
    
  
    
def xrand(head,tail=0):
  
  if tail < head:
    head, tail = tail, head ##tmp = head; head = tail; tail = tmp  
  
  tail -= 1
  leng = tail-head+1
  temp = []
  while len(list(set(temp))) < leng:
    num = random.randint(head, tail)
    temp.append(num)
  
  res = []
  for i in temp:
    if i not in res:
      res.append(i)
  
  return res
  
  
  
  
  
def allwords(wbox):
  words = []
  for i in wbox:
    words.append(i[0])
  return words    

  

  
def dicts(voc, wbox):
  for data in wbox:
    if voc.lower() == data[0]:
      print(logo,'%s %s'%(voc,data[1]))

     
  
  
def main():

  os.system('color b')
  mark()
  welcome()
  filename = '7000vocs.csv'  
  wordbox = csvin(filename) 
  words = allwords(wordbox)  

  while True:
    cmd = input('%s '%logo)
    cmds = [['exit()'],
            ['help','?','-h'],
            ['stat'],
            ['quiz'],
			['exam']]
    if cmd.lower() in cmds[0] :
      exit()
      break
    elif cmd.lower() in cmds[1]:
      help()  
    elif cmd.lower() in cmds[2]: 
      statistics(wordbox)
    elif cmd.lower() in cmds[3]:	
      quiz(wordbox)
    elif cmd.lower() in cmds[4]:
      level = int(input('%s level:'%logo))
      exam(wordbox,level)
    elif cmd.lower() in words:
      dicts(cmd, wordbox)  
    else:
      continue    

  
 

 
#######################################################################################
 
 
 

logo = 'c0xffee>>>' 
main()
    
    
  
    
    
    
    
    