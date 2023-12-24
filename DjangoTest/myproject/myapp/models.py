from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        item = cls(name=name)
        item.save()
        return item