from django.views.generic import View
from django.http import JsonResponse
from menu.models import Menu
import json

# Create your views here.
class MenuView(View):
    def post(self, request):
        try:
            # TODO 1 : 비어 있는 param 가 없는 지 검증..
            req_body = json.loads(request.body)
            param_dict = {}
            param_dict['date'] = json.loads(req_body.get('action').get('params').get('date')).get('date')
            param_dict['cycle'] = req_body.get('action').get('params').get('cycle')
            param_dict['location'] = req_body.get('action').get('params').get('location')
            #param_dict['test'] = req_body.get('action').get('params').get('test')
            for key, value in param_dict.items():
                if value is None:
                    raise Exception(key)
        except Exception as e:
            return JsonResponse({
                        'version': '2',
                        'data': {},
                        } ,status=200)
        try:
            # TODO 2 : param 으로 3개 값 받기(date, cycle, location)
            menu_obj = Menu.objects.get(date=param_dict['date'], cycle=param_dict['cycle'], location=param_dict['location'])
            #menu_obj = Menu.objects.get(date=param_dict['date'], cycle=param_dict['cycle'], location=param_dict['location'],test=param_dict['test'])
        except Exception:
            return JsonResponse({
                        'version': '2',
                        'data': {},
                        } ,status=200)
        # TODO 3 : 요청 param 에 일치하는 queryset 추출 후 json 응답 #ㅎㅎ
        return JsonResponse({
            'version': '2',
            'data': {
                'menu1': menu_obj.menu1,
                'menu2': menu_obj.menu2,
                'menu3': menu_obj.menu3,
                'menu4': menu_obj.menu4,
                'menu5': menu_obj.menu5,
            }
        })