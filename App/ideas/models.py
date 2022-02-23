from django.db import models

IDEA_STATUS = (
    ('pending', 'Waiting for rewiew'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected')
)


class Idea(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    app_url = models.URLField(null=True, blank=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=30, default='pending')

    def __str__(self):
        return self.title


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f'Vote ID: {self.id}'
