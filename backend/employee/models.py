from django.contrib.gis.db.models import PointField
from django.db import models
from django.utils.safestring import mark_safe


class Employee(models.Model):
    id = models.AutoField(name="id", primary_key=True, unique=True, db_index=True)
    first_name = models.CharField(name="first_name", null=False, max_length=255)
    last_name = models.CharField(name="last_name", null=False, max_length=255)
    position_title = models.CharField(name="position_title", null=False, max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.position_title}"


class Branch(models.Model):
    id = models.AutoField(name="id", primary_key=True, unique=True, db_index=True)
    name = models.CharField(name="name", max_length=255)
    facade_image = models.ImageField(name="facade_image")
    position = PointField()
    employees = models.ManyToManyField(Employee)

    def image_tag(self):
        return mark_safe(
            f'<img src="{self.facade_image.url}" width="150" height="150" />'
        )

    image_tag.short_description = "Image"

    def __str__(self) -> str:
        return f"{self.name}"
