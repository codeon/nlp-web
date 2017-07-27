from django.http import HttpResponse
from django.views import View

# Create your views here.

from spacy import *

class TextParser(View):
    """
    Class for generic endpoints
    """

    def get(self, request):
        # input_str = request.data['input']
        # en_nlp = spacy.load('en')
        # en_doc = en_nlp(input_str)
        return HttpResponse("This is output.")
        