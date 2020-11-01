from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()

    def shortSummary(self):
        shorttext = self.summary[:100]
        if shorttext.endswith(' ')==False:
            shorttext = shorttext[:shorttext.rfind(' ')]
        shorttext = shorttext+"..."
        return shorttext
