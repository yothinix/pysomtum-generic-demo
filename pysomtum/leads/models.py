from django.db import models


class Lead(models.Model):
    CONTACT_METHOD = (
        ('phone', 'Via Phone'),
        ('email', 'Via Email'),
    )
    first_name = models.CharField(null=False, blank=False, max_length=256)
    last_name = models.CharField(null=False, blank=False, max_length=256)
    email = models.EmailField(null=False, blank=False, max_length=256)
    phone = models.CharField(null=False, blank=False, max_length=256)
    prefered_contact_method = models.CharField(
        choices=CONTACT_METHOD, null=False, blank=False, max_length=256)
    message = models.TextField(null=True, blank=True)

