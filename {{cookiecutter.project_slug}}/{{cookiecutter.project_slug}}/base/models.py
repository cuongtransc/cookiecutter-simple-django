from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """
    created_at = AutoCreatedField()
    modified_at = AutoLastModifiedField()

    class Meta:
        abstract = True
