from django.db import models
from django.utils.timezone import now

def current_time():
    return now().time()
# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.dept_name

class Log(models.Model):
    status_choices = {
        "PENDING":"PENDING",
        "COMPLTED":"COMPLETED"
    }
    date = models.DateField(default=now)
    time = models.TimeField(default=current_time)
    context = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=status_choices)
    action = models.TextField()
    guidance = models.TextField()
    
    def __str__(self):
        return f"{self.dept.dept_name} - {self.person} - {self.status}"
    