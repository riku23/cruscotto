from django.db import models


class Url(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)


    def __unicode__(self):
        return self.name



class Test(models.Model):
    url_id = models.ForeignKey(Url)
    test_string = models.TextField()

    def __unicode__(self):
        return "Test "+ self.url_id.name





class Verifica(models.Model):
    url_id = models.ForeignKey(Url)
    risultato = models.BooleanField()
    data_ora = models.DateTimeField()

    def __unicode__(self):
        return "Verifica "+self.url_id.name