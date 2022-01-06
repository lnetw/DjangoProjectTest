from django.db import models


class DataSet(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return str(self.id)
