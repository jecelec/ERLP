from django.db import models
from .user     import User

class Historico(models.Model):
    id                    = models.AutoField(primary_key=True)
    departamento          = models.CharField('departamento',  max_length = 56)
    municipio             = models.CharField('municipio',     max_length = 56)
    codigo_arl            = models.IntegerField(default=1423)
    year                  = models.IntegerField()
    month                 = models.IntegerField()
    economia              = models.IntegerField()
    rela_dep              = models.IntegerField()
    rela_indep            = models.IntegerField()
    presu_acci_rasu       = models.IntegerField()
    muertes_AT            = models.IntegerField()
    pensiones_AT          = models.IntegerField()
    pensiones_EL          = models.IntegerField()
    incapacidades_EL      = models.IntegerField()
    incapacidades_AT      = models.IntegerField()