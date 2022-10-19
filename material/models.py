from django.db import models

class Material(models.Model):
    type = models.CharField(max_length=50, choices=[("wood", "Wood"), ("metal", "Metal"), ("plastic", "Plastic")])
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    diameter = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type} {self.length}x{self.width}x{self.height} {self.diameter} {self.quantity}"