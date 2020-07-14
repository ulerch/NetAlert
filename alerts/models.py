from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Nature(models.Model):
    index = models.PositiveIntegerField()
    name = models.CharField(max_length=40)
    descr_en = models.CharField(max_length=100)
    descr_de = models.CharField(max_length=100)
    descr_fr = models.CharField(max_length=100)
    descr_it = models.CharField(max_length=100)
    descr_rm = models.CharField(max_length=100)

    class Meta:
        ordering = ['index']

    def __str__(self):
        return '%s - %s' % (self.index, self.name)


class Origin(models.Model):
    index = models.PositiveIntegerField()
    name = models.CharField(max_length=40)
    descr_en = models.CharField(max_length=100)
    descr_de = models.CharField(max_length=100)
    descr_fr = models.CharField(max_length=100)
    descr_it = models.CharField(max_length=100)
    descr_rm = models.CharField(max_length=100)

    class Meta:
        ordering = ['index']

    def __str__(self):
        return '%s - %s' % (self.index, self.name)


class Alert(models.Model):
    nature = models.ForeignKey(Nature, on_delete=models.PROTECT)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT)
    description = models.TextField()
    url = ArrayField(models.URLField(max_length=200))
    email = models.EmailField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s - %s / %s' % (self.created_at, self.nature.name, self.origin.name)


REVISION_TYPE_NOTE = 'NOTE'
REVISION_TYPE_ACTION = 'ACTION'
REVISION_TYPE_PROGRESS = 'PROGRESS'
REVISION_TYPE_FEEDBACK = 'FEEDBACK'
REVISION_TYPE_SOLVED = 'SOLVED'
REVISION_TYPE_CLOSED = 'CLOSED'

REVISION_TYPE_CHOICES = (
    (REVISION_TYPE_NOTE, 'Note'),
    (REVISION_TYPE_ACTION, 'Action'),
    (REVISION_TYPE_PROGRESS, 'Progress'),
    (REVISION_TYPE_FEEDBACK, 'Feedback'),
    (REVISION_TYPE_SOLVED, 'Solved'),
    (REVISION_TYPE_CLOSED, 'Closed')
)


class Revision(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    revision_type = models.CharField(
        max_length=10, choices=REVISION_TYPE_CHOICES, default=REVISION_TYPE_NOTE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s: %s' % (self.user, self.created_at)
