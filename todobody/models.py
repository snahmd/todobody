from django.db import models

# Create your models here.




class Todo(models.Model):
    AREA = (
        (1, "Gögüs"),
        (2, "Arka Kol"),
        (3, "Bacak"),
        (4, "Omuz"),
        (5, "Sirt"),
        (6, "Ön Kol"),
        (7, "Karin"),
        (8, "Bel"),
        (9, "Kardiyo"),
    )
    area = models.SmallIntegerField(choices=AREA, default=1)
    task = models.CharField(max_length=150)
    description = models.CharField(max_length=300) 
    is_done = models.BooleanField(default=False)
