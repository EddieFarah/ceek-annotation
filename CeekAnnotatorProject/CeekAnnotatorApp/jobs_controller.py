import os, sys
from api_loader import ApiLoader
from django.http import JsonResponse

APPLICATION_ID = "APPLICATION_ID_HERE"
REST_API_KEY = "REST_API_KEY_HERE"

adsApiLoader = ApiLoader()

class JobsController(object):

    def get_job_offers_list(self, request):
        try:
            account_info = adsApiLoader.load_offers()

            return JsonResponse({'status':'success','result':account_info})
        except Exception, e:
            return JsonResponse({'error':str(e),'status':'error'})

    def retrieve_job_offers_list(self, request):
        try:
            retrieved_offers = adsApiLoader.retrieve_offers()

            return JsonResponse({'status':'success','result':retrieved_offers})
        except Exception, e:
            return JsonResponse({'error':str(e),'status':'error'})

    def annotate_job_offer(self, request):
        try:
            text = request.GET.get('text',None)
            annotated_offer = adsApiLoader.annotate_offer(text)
            return JsonResponse({'status':'success','result':annotated_offer})
        except Exception, e:
            return JsonResponse({'error':str(e),'status':'error'})

    def filter_job_offers(self, request):
        try:
            company = request.POST.get('company',None)
            location = request.POST.get('location',None)
            position = request.POST.get('position',None)

            filtered_offers = adsApiLoader.filter_offers(company,location,position)
            return JsonResponse({'status':'success','result':filtered_offers})
        except Exception, e:
            return JsonResponse({'error':str(e),'status':'error'})