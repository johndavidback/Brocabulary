from django.shortcuts import render_to_response
from django.template.context import RequestContext

from brocab.models import Word
# Create your views here.

def index(request):
    words = Word.objects.all().order_by('word')
    context = RequestContext(request, {
        'words': words,
    })

    return render_to_response('index.html', context)