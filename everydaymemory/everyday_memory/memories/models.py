from django.db import models
from django.utils import timezone
import datetime
import os 
import pathlib
# Create your models here.

MEMORIES_PHOTOS_PATH = "memories_photo"

RATE_DAY = (
    ("HORRIBLE","HORRIBLE"),
    ("BAD","BAD"),
    ("OK","OK"),
    ("GOOD","GOOD"),
    ("AWESOME","AWESOME")
)

class Memory(models.Model):
    one_line_description = models.CharField(help_text="Describe your day in 1 line",default="Meh..",max_length=200)
    how_was_the_day = models.CharField(choices=RATE_DAY,default=RATE_DAY[2][1],max_length=50)
    date_time = models.CharField(default=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),max_length=200)
    image = models.FileField(upload_to=MEMORIES_PHOTOS_PATH,default=os.path.join(MEMORIES_PHOTOS_PATH,'default.jpg'))
    special_comments = models.TextField(blank=True)


    class Meta:
        verbose_name = "Memory"
        verbose_name_plural = "Memories"

    def __str__(self):
        return self.date_time

    def save(self, *args, **kwargs):
        print('save() is called.')
        
        # self.image.name = os.path.join(MEMORIES_PHOTOS_PATH,self.date_time)
        self.date_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.image.name = self.date_time+pathlib.Path(self.image.name).suffix
        # self.image.save()
        super(Memory, self).save(*args, **kwargs)



