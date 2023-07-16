from celery import Celery
from .parser import ghparser,ghscarper

app = Celery('tasks', backend='://localhost', broker='pyamqp://guest@localhost//',)
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task
def parser(name):
    return ghparser(name)


@app.task
def scarper(name):
    return ghscarper(name)

if __name__ == '__main__':
    print(ghparser('elvgarrui'))

