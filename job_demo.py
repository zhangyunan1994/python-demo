from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    print('job 3s')
    time.sleep(5)

def job2():
    print('job ASSs')
    time.sleep(5)


if __name__=='__main__':

    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    scheduler.add_job(job, 'interval', id='3_second_job', seconds=3)
    scheduler.add_job(job2, id='3_second_job2' , trigger='cron', minute='0-59')
    scheduler.start()

    while(True):
        print('main 1s')
        time.sleep(1)
