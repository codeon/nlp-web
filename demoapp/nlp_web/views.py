from django.http import JsonResponse
from django.views import View

# Create your views here.
import nltk
from nltk.corpus import *


class TextParser(View):
    """
    Class for generic endpoints
    """

    def get(self, request):
        text = request.GET.get('input', '')
        tokens = nltk.word_tokenize(text.lower())
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(text)
        return JsonResponse(dict(tags))
