from django.views.generic import View
from django.http import JsonResponse
from menu.models import Menu

# Create your views here.
class MenuView(View):
    def get(self, request):
        try:
            # TODO 1 : 비어 있는 param 가 없는 지 검증
            param_dict = {}
            param_dict['date'] = request.GET.get('date')
            param_dict['cycle'] = request.GET.get('cycle')
            param_dict['location'] = request.GET.get('location')
            for key, value in param_dict.items():
                print(key)
                print(value)
                if value is None:
                    raise Exception(key)       
        except Exception as e:
            return JsonResponse({
                        'error': '1',
                        'message': f'{e} 입력 값이 없습니다!'
                        } ,status=400)
        try:
            # TODO 2 : param 으로 3개 값 받기(date, cycle, location)
            menu_obj = Menu.objects.get(date=request.GET.get('date'), cycle=request.GET.get('cycle'), location=request.GET.get('location'))
        except Exception:
            return JsonResponse({
                        'error': '1',
                        'message': '조건에 맞는 메뉴가 없습니다!'
                        } ,status=500)
        # TODO 3 : 요청 param 에 일치하는 queryset 추출 후 json 응답
        return JsonResponse({
            'error': '0',
            'message': {
                'menu1': menu_obj.menu1,
                'menu2': menu_obj.menu2,
                'menu3': menu_obj.menu3,
                'menu4': menu_obj.menu4,
                'menu5': menu_obj.menu5,
            }
        })