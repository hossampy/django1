from django.db import models

job_type = (
    ('full time', 'full time'),
    ('part time', 'part time'),
)


class job(models.Model):
    title = models.CharField(max_length=100)
    job_typ = models.CharField(max_length=15, choices=job_type)
    desctiption = models.TextField(max_length=1000)
    publishat = models.DateTimeField(auto_now=True)
    vanacy = models.IntegerField(default=1)
    expirince = models.IntegerField(default=1)
    salry = models.IntegerField(default=1000)
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class category(models.Model):

    Name = models.CharField(max_length=25)

    def __str__(self):
        return self.Name
