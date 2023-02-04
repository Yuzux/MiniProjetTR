#task 1 periode 10 sec execution 1 sec
#task 2 periode 10 sec execution 1 sec
#task 3 periode 60 sec execution 20 sec
#task 4 periode 30 sec execution 20 sec

import sched, time
import time
import datetime

#defining the scheduler
s = sched.scheduler(time.time, time.sleep)

#defining the tasks
def task1(sc):
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : Task 1 executed")
    s.enter(10, 1, task1, (sc,))
def task2(sc):
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : Task 2 executed")
    s.enter(10, 1, task2, (sc,))
def task3(sc):
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : Task 3 executed")
    s.enter(60, 20, task3, (sc,))
def task4(sc):
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : Task 4 executed")
    s.enter(30, 20, task4, (sc,))
    print(datetime.datetime.now().strftime("%H:%M:%S") + " : Task 4 ended")
#defining the main function
def main():
    s.enter(0, 1, task1, (s,))
    s.enter(0, 1, task2, (s,))
    s.enter(0, 1, task3, (s,))
    s.enter(0, 1, task4, (s,))
    s.run()
#calling the main function
if __name__ == "__main__":
    main()
    