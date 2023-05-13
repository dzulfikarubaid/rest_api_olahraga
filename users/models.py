from django.db import models

# Create your models here.
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    nama_cabang = models.CharField(max_length=100)
    deskripsi = models.TextField()
    sejarah = models.TextField()

    def __str__(self):
        return str(self.id) + " | "+self.nama_cabang