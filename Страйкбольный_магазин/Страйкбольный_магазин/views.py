from django.shortcuts import render
from Страйкбольный_магазин.Страйкбольный_магазин.models import Weapon, Creater
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse

class IndexListView (ListView):
    model = Weapon
    template_name = "index.html"
    context_object_name = "weapon"

def catalog(request: HttpRequest):
    # Достаю параметр маршрута
    Creater = request.GET.get("author")
    if (Creater):
        Weapon = Weapon.objects.filter(Creaters=Creater)
    else:
        Weapon = Weapon.objects.all()
    return render(request, "catalog.html", {"Weapon": Weapon})

def api_get_all_authors(request):
    authors = Creater.objects.all()
    dataList = [author.parse_object() for author in authors]
    # safe - чтобы отправить в качестве ответа массив, а не объект, как этого требует JsonResponse
    return JsonResponse(dataList, safe=False)
    
