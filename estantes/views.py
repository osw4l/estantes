from django.shortcuts import render
from .models import Estante
from django.shortcuts import _get_queryset
# Create your views here.




def get_object_or_none(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except:
        return None


def home(request):
	if request.POST:
		dato = request.POST.get('dato')
		print(dato)
		estante = get_object_or_none(Estante, referencias=dato)
		if estante:
			return render(request, 'index.html', {'estante': estante})
		else:
			estante = get_object_or_none(Estante, codigo=dato)
			if estante:
				return render(request, 'index.html', {'estante': estante})
			else:
				return render(request, 'index.html', {'estante': False, 'error':True})
	return render(request, 'index.html')

