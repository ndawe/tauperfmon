from variables.models import Variable
from django.shortcuts import render_to_response

def variable_list(request):
    variables = Variable.objects.all()
    return render_to_response('variables/index.html', {'variables': variables})
