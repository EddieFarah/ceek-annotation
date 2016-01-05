from django.http import JsonResponse

class DataBaseController(object):

    def get_app_id(self, request):
        return JsonResponse({'status':'success'})