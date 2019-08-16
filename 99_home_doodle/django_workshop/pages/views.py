from django.shortcuts import render

# Create your views here.
def pushnumber(request):
    return render(request, 'pushnumber.html')

def pullnumber(request):
    m =  request.GET.get('number')
    context = {'number': m,}
    return render(request, 'pullnumber.html', context)
