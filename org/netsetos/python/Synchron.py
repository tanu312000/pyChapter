import threading as t
lock=t.Lock()
class Thread1(t.Thread):
    def sun(self):
        i=1
        while(i<=10):
            if(i<=5):
                pass
            else:
                lock.aquire()
                print("Thread1",i,end='\n')
                i=i+1
                lock.release()

t=Thread1()
t2=Thread1()
t3=Thread1()
t.start()
t2.start()
t3.start()