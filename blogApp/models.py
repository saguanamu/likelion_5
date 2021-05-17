from django.db import models

#class Plan(models.Model):
#    title = models.CharField(max_length=200)
#    departDate = models.DateField(blank=True, default=timezone.now, null=True)
#    arriveDate = models.DateField(blank=True, default=timezone.now, null=True)
#    password = models.CharField(max_length=200)
#    hotel = models.CharField(max_length=200)
#    created_at = models.DateTimeField('작성시간', default = timezone.now)
#    updated_at = models.DateTimeField('수정시간', default = timezone.now)
#    view_count = models.IntegerField(default=0)
#    scrap_users = models.ManyToManyField(User, through='Scrap', related_name = 'scrap_plans')
#    scrap_count = models.PositiveIntegerField(default=0)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]