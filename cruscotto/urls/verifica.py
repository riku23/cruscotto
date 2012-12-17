from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from cruscotto.models import Verifica

verifica_info = {'queryset': Verifica.objects.all() }

urlpatterns = patterns('',
    url(r'^$',
        object_list,
        dict(verifica_info, paginate_by=20),
        name='cruscotto_verifica_list'),
)