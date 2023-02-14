from django.db import models
class Togri(models.Model):
    soz=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.soz}"
class Xato(models.Model):
    notogri=models.CharField(max_length=40)
    stogri_fk=models.ForeignKey(Togri,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.notogri}"


