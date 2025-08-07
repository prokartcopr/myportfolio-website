from django.db import models

class CV(models.Model):
    title = models.CharField(max_length=100, default="My CV")
    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title