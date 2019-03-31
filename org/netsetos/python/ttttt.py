# import threading as t
# class Thread1(t.Thread):
#     def runs123(self):
#         i=1
#         while(i<=10):
#             print("Thread ",i,end='\n')
#             i=i+1
# t1=Thread1()
# t2=Thread1()
# t1.start()
# t2.start()

import threading as t
lock=t.Lock()
class Threadi1(t.Thread):
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

t=Threadi1()
t2=Threadi1()
t3=Threadi1()
t.start()
t2.start()
t3.start()