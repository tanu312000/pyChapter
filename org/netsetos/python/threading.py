

import threading as t
class Thread1(t.Thread):
    def run(self):
        i=1
        while(i<=10):
            print("Thread ",i,end='\n')
            i=i+1
t1=Thread1()
t2=Thread1()
t1.start()
t2.start()
