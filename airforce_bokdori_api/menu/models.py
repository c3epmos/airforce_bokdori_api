from django.db import models

# Create your models here.
class Menu(models.Model):
    cycle_choices = (
        ('조식', '조식'),
        ('중식', '중식'),
        ('석식', '석식')
    )
    location_choices = (
        ('독수리회관', '독수리회관'),
        ('시루정', '시루정')
    )

    date = models.DateField()
    cycle = models.CharField(max_length=100, choices=cycle_choices)
    location = models.CharField(max_length=100, choices=location_choices)
    menu1 = models.CharField(max_length=100, null=True, blank=True)
    menu2 = models.CharField(max_length=100, null=True, blank=True)
    menu3 = models.CharField(max_length=100, null=True, blank=True)
    menu4 = models.CharField(max_length=100, null=True, blank=True)
    menu5 = models.CharField(max_length=100, null=True, blank=True)
