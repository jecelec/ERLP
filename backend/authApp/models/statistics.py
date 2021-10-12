from django.db import models
from .user     import User

class Account(models.Model):
    id                    = models.AutoField(primary_key=True)
    dpto                  = models.CharField('dpto',     max_length = 30)
    mpio                  = models.CharField('mpio',     max_length = 30)
    codArl                = models.IntegerField(default=1423)
    anoInforme            = models.DateTimeField()
    mesInforme            = models.IntegerField()
    activec               = models.IntegerField()
    rela_dep              = models.IntegerField()
    rela_indep            = models.IntegerField()
    presuAccide           = models.IntegerField()
    muertesRepAT          = models.IntegerField()
    nuevaPensionInva_R_AT = models.IntegerField()
    nuevaPensionInva_R_EL = models.IntegerField()
    incaPermaParciar_AT   = models.IntegerField()
    incaPermaParciar_EL   = models.IntegerField()
    isActive              = models.BooleanField(default=True)
    lastChangeDate        = models.DateTimeField()