from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=2000)
    article_uuid = models.CharField(max_length=20)
    comment_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment_text

'''
class Article(models.Model):
    promo = models.TextField()
    body = models.TextField()
    headline = models.CharField(max_length=300)
    byline = models.CharField(max_length=300)
    image_url = models.CharField(max_length=500)
    pitch_text = models.CharField(max_length=500)
    publish_at = models.DateTimeField('published date')
    uuid = models.CharField(max_length=200)
    instruments = models.CharField(max_length=500)

    def __str__(self):
        return self.headline

    class meta:
        managed = False

'''