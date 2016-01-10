__author__ = 'Edie'

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from jobs_controller import JobsController
from django.views.decorators.csrf import csrf_exempt
import views

jobsController = JobsController()

urlpatterns = [
    #url(r'^test_database/$', accountsController.get_test_database),
    # App Calls
    url(r'^job_offers/list/$', jobsController.get_job_offers_list),
    url(r'^job_offers/retrieve/list/$', jobsController.retrieve_job_offers_list),
    url(r'^job_offers/annotate/$', jobsController.annotate_job_offer),
    url(r'^job_offers/filter/$', csrf_exempt(jobsController.filter_job_offers)),
    url(r'^index/$', views.index)
]