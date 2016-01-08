__author__ = 'Edie'

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from jobs_controller import JobsController

jobsController = JobsController()

urlpatterns = [
    #url(r'^test_database/$', accountsController.get_test_database),
    # App Calls
    url(r'^job_offers/list/$', jobsController.get_job_offers_list),
    url(r'^job_offers/retrieve/list/$', jobsController.retrieve_job_offers_list),
    url(r'^job_offers/annotate/$', jobsController.annotate_job_offer)
]