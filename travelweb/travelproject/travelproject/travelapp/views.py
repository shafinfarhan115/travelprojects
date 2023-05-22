
from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    abj=team.objects.all()

    return render(request,"index.html",{'result':obj,'travel':abj})















#def operation(request):
 #  x=int(request.GET['num1'])
 #  y=int(request.GET['num2'])
 #   add=x+y
 #   sub=x-y
   # div=x/y
   ## mul=x*y
  #  return render(request,"result.html",{'addition':add,'subtract':sub,'division':div,'multiplication':mul})