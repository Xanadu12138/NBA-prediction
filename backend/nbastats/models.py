from django.db import models
from django.conf import settings
import os

# Create your models here.
class Teamlist(models.Model):
    ran = models.IntegerField(db_column='Ran', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    suc = models.IntegerField(db_column='Suc', blank=True, null=True)  # Field name made lowercase.
    neg = models.IntegerField(db_column='Neg', blank=True, null=True)  # Field name made lowercase.
    sucave = models.CharField(db_column='SucAve', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dif = models.TextField(db_column='Dif', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hom = models.CharField(db_column='Hom', max_length=6, blank=True, null=True)  # Field name made lowercase.
    awa = models.CharField(db_column='Awa', max_length=6, blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='Di', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sco = models.TextField(db_column='Sco', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    los = models.TextField(db_column='Los', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mar = models.TextField(db_column='Mar', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sn = models.CharField(db_column='SN', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teamlist'
    
    def __str__(self):
        return '%s' % self.tm

class Playersinfo(models.Model):
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=20)  # Field name made lowercase.
    num = models.CharField(db_column='Num', blank=True, null=True, max_length=20)  # Field name made lowercase.
    pos = models.CharField(db_column='Pos', blank=True, null=True, max_length=20)  # Field name made lowercase.
    tall = models.CharField(db_column='Tall', blank=True, null=True, max_length=20)  # Field name made lowercase.
    wei = models.CharField(db_column='Wei', blank=True, null=True, max_length=20)  # Field name made lowercase.
    bri = models.CharField(db_column='Bri', blank=True, null=True, max_length=20)  # Field name made lowercase.
    tm = models.ForeignKey(Teamlist,db_column='Tm',on_delete=models.CASCADE) # Field name made lowercase.
    con = models.CharField(db_column='Con', blank=True, null=True, max_length=20)  # Field name made lowercase.
    img = models.URLField(db_column='Img', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playersinfo'

    def __str__(self):
        return '%s' % self.name


class Playersper(models.Model):
    playername = models.CharField(db_column='PlayerName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=8, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='Pos', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    mp = models.CharField(db_column='MP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fg = models.CharField(db_column='FG', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fga = models.CharField(db_column='FGA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fgaver = models.CharField(db_column='FGAver', max_length=5, blank=True, null=True)  # Field name made lowercase.
    number_3p = models.CharField(db_column='3P', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3pa = models.CharField(db_column='3PA', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3paver = models.CharField(db_column='3PAver', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2p = models.CharField(db_column='2P', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2pa = models.CharField(db_column='2PA', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2paver = models.CharField(db_column='2PAver', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    efgaver = models.CharField(db_column='eFGAver', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ft = models.CharField(db_column='FT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fta = models.CharField(db_column='FTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ftaver = models.CharField(db_column='FTAver', max_length=5, blank=True, null=True)  # Field name made lowercase.
    orb = models.CharField(db_column='ORB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    drb = models.CharField(db_column='DRB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    trb = models.CharField(db_column='TRB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ast = models.CharField(db_column='AST', max_length=5, blank=True, null=True)  # Field name made lowercase.
    stl = models.CharField(db_column='STL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    blk = models.CharField(db_column='BLK', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tov = models.CharField(db_column='TOV', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pf = models.CharField(db_column='PF', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pts = models.CharField(db_column='PTS', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playersper'


class Schlist(models.Model):
    tm1 = models.CharField(db_column='Tm1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tm2 = models.CharField(db_column='Tm2', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sco1 = models.CharField(db_column='Sco1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sco2 = models.CharField(db_column='Sco2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sco = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schlist'


