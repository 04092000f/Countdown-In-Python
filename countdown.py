from datetime import datetime
import time
def date(x):
    lst = []
    l1 = []
    
  
    for i in range(0, x): 
        date = input("Date : ")
        date=date.replace('.','/')
        time =input("Time : ") 
        lst.append(date)
        l1.append(time)
    return lst,l1


def date_time(ls1,ls2):
    fl=[]
    for i in ls1:
        for j in ls2:
            date_time_str = i+" "+j
            date_time_obj = datetime.strptime(date_time_str,'%d/%m/%y %H:%M:%S')
            fl.append(date_time_obj)
            fl=tuple(fl)
    return fl

def dt_to_ut(fl,list1,list2):
    conv=[]
    fl=date_time(list1,list2)
    for i in fl:
        secs = int(i.timestamp())
        conv.append(secs)
    return conv

def countdown(con):
    for i in con:
        present = datetime.now()
        present = int(present.timestamp())
        future = i
        difference = future - present
        while difference:
            mins, secs = divmod(difference, 60)
            timeformat = '{:02f}:{:02f}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            difference -= 1
        print("\nThe date has been reached!")
        
         


n = int(input("Enter number of elements : ")) 
l1,l2=date(n)
print(l1)
f1=date_time(l1,l2)
print(f1)
uni=dt_to_ut(f1,l1,l2)
print(uni)
countdown(uni)
