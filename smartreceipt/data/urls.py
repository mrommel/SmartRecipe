from django.conf.urls import patterns, url

from data import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/index/')),
    url(r'^index/', views.index, name='data.views.index'),
    url(r'^receipts/', views.receipts, name='data.views.receipts'),
    url(r'^receipt/(?P<receipt_id>\d+)', views.receipt, name='data.views.receipt'),
    url(r'^category/(?P<category_id>\d+)', views.category, name='data.views.category'),
    url(r'^categories/', views.categories, name='data.views.categories'),
    url(r'^integrient_search', views.integrient_search, name='data.views.integrient_search'),
    url(r'^receipts_by_integrients', views.receipts_by_integrients, name='data.views.receipts_by_integrients'),
)