from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Feature(models.Model):
    PRODUCT_AREA = (
        ("Assessments", "Assessments"),
        ("Billing", "Billing"),
        ("Recruit", "Recruit"),
        ("Reports", "Reports")
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    client_priority = models.IntegerField()
    target_date = models.DateField()
    product_area = models.CharField(max_length=50, choices=PRODUCT_AREA)

    def __str__(self):
        return self.title
    