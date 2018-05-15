from dataMining import views
from django.conf.urls import url


urlpatterns = [
	url(r'^result/$', views.preMine, name='result'),
	url(r'^(?P<year>[0-9]{4})/(?P<id>[\w\-.]+)/$', views.getIndicator, name='getIndicator'),
	url(r'^(?P<year>[0-9]{4})/(?P<id>[\w\-.]+)/(?P<my_country>[\w]+)/$', views.getIndex, name='getIndex'),
	# url(r'^indicators/$', views.IndicatorList.as_view(), name='indicators'),
	# url(r'^fill/indicators/$', views.fill_indicators_table, name="fill_indicatos")
]

# urlpatterns = format_suffix_patterns(urlpatterns)