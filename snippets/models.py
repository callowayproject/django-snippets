from django.db import models

class Snippet(models.Model):
    """A text snippet. Not meant for use by anyone other than a designer"""
    
    name = models.CharField(max_length=255)
    snippet = models.TextField(blank=True)
    
    class Meta:
        pass
    
    def __unicode__(self):
        return self.snippet
