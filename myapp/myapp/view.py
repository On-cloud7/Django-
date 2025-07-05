from django.http import HttpResponse

import datetime
def test(request):
    date= datetime.dtaetime.now()
    print("test function is called from view")
    return HttpResponse("<h1>Hello this is index page<h1>"+str(date))
