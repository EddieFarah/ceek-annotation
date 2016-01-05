__author__ = 'Edie'

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from database_controller import DataBaseController

accountsController = DataBaseController()

urlpatterns = [
    #url(r'^test_database/$', accountsController.get_test_database),
    # App Calls
    url(r'^apps/list/$', accountsController.get_app_id),
]