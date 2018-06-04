from django.db import models

class Account(models.Model):
	user_name = models.CharField(max_length = 80)
	password = models.CharField(max_length = 255)
	reg_data = models.DataField()

	def __unicode__(self):
		return "Account: %s" %self.user_name

class Contact(models.Model):
	account = models.OneToOneField(
			Account,
			on_detele = models.CASCADE,
			primary_key = True
		)
	# account = models.ForeignKey(Account,on_detele = models.CASCADE)
	# accounts = models.ManyToManyField(Account)
	zip_code = models.CharField(max_length = 10)
	address = models.CharField(max_length = 80)
	mobile = models.CharField(max_length = 20)

	def __unicode__(self):
		return "%s,%s" % (self.account.user_name,mobile)


from django.conf.urls import include, url

urlpatterns = (
		url(r'^year/2015/$', views.year_moments, name = 'moments_2015')
	)

<a href="{% url 'moments_2015' %}">查看2015年消息</a>

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def redirect_to_year_2015(request):
	return HttpResponseRedirect(reverse('moments_2015'))



