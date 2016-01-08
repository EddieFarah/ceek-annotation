__author__ = 'Edie'
import json
from django.db import models

class JobOffer(models.Model):
    Id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    compnay_url = models.CharField(max_length=100)
    compnay_logo = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    how_to_apply = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Id

    @classmethod
    def create(cls, id,title,description,compnay_url,compnay_logo,created_at,company,how_to_apply,location,url,type):
        ad= cls(Id=id,title=title,description=description,compnay_url=compnay_url,compnay_logo=compnay_logo,created_at=created_at,company=company,
                how_to_apply=how_to_apply,location=location,url=url,type=type)
        # do something with the book
        return ad

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=0, separators=(',', ': '))