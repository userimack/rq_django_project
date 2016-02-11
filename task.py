from django_rq import job

@job
def fun():
    print ("Hello mack")
    print("Welcome to the queue!!")
