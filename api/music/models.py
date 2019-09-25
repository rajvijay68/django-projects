from django.db import models 


class Songs(models.Model):
    title = models.CharField(max_length=255,null=False)
    artist = models.CharField(max_length=255,null=False)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
    def __str__(self):
        return "{} - {}".format(self.title,self.artist)