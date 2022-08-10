from flask import Flask

from covid_app import app
from covid_app.views import my_scheduled_job

from apscheduler.schedulers.background import BackgroundScheduler
schedule_task = BackgroundScheduler()



if __name__ == "__main__":
    schedule_task.add_job(my_scheduled_job, 'interval', minutes=60)
    schedule_task.start() 
    app.run(debug=True, host="0.0.0.0", port=5000)