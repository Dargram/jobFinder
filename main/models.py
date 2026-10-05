from django.db import models

class Vacancies(models.Model):
    position     = models.CharField(max_length=255)
    company      = models.CharField(max_length=255)
    requirements = models.TextField()
    descriptions = models.TextField()
    created_at   = models.DateTimeField()
    recorded_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} is in {self.company}"