from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        shorttext = self.body[:70]
        if shorttext.endswith(' ')==False:
            shorttext = shorttext[:shorttext.rfind(' ')]
        shorttext = shorttext+"..."
        return shorttext

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
