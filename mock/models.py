from __future__ import unicode_literals

from django.db import models

# Create your models here.


import json
class Project(models.Model):
    name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name

    def to_obj(self):

        table = dict()
        table_set = self.table_set.all()
        for t in table_set:
            table[t.name] = t.to_obj()
        return dict(
            name = self.name,
            table=table,
            database_id=self.id
        )

class Table(models.Model):
    name = models.CharField(max_length=32)
    database = models.ForeignKey(Project)

    def __unicode__(self):
        return self.database.name + '->' +self.name

    def to_obj(self):



        return dict(
            colnum=[c.name for c in self.colnum_set.all()],
            row=[r.get_data() for r in self.row_set.all()],
            table_id=self.id
        )

class Colnum(models.Model):
    name = models.CharField(max_length=32)
    table = models.ForeignKey(Table)
    def __unicode__(self):
        return self.table.database.name + '->' +self.table.name + '->' + self.name



class Row(models.Model):
    data = models.TextField()
    table = models.ForeignKey(Table)


    def __unicode__(self):
        return self.table.database.name + '->' + self.table.name + '->' + str(self.id)

    def get_data(self):
        obj = json.loads(self.data)
        obj['id'] = self.id
        return obj

