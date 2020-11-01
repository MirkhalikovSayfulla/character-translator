from django.shortcuts import render
from django.http import HttpResponse
from transliterate import translit, get_available_language_codes
from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class TranslateView(View):
    result = ''

    def get(self, request, *args, **kwargs):
        if self.kwargs['translatorCh'] == 'latinToCyrillic':
            fromL = 'Latin'
            toL = 'Cyrillic'

        elif self.kwargs['translatorCh'] == 'latinToGeorgian':
            fromL = 'Latin'
            toL = 'Georgian'

        elif self.kwargs['translatorCh'] == 'latinToArmenian':
            fromL = 'Latin'
            toL = 'Armenian'

        elif self.kwargs['translatorCh'] == 'latinToGreek':
            fromL = 'Latin'
            toL = 'Greek'

        elif self.kwargs['translatorCh'] == 'cyrillicToLatin':
            fromL = 'Cyrillic'
            toL = 'Latin'

        elif self.kwargs['translatorCh'] == 'georgianToLatin':
            fromL = 'Georgian'
            toL = 'Latin'

        elif self.kwargs['translatorCh'] == 'armenianToLatin':
            fromL = 'Armenian'
            toL = 'Latin'

        elif self.kwargs['translatorCh'] == 'greekToLatin':
            fromL = 'Greek'
            toL = 'Latin'

        context = {
            'result': self.result,
            'fromL': fromL,
            'toL': toL
        }
        return render(request, 'translator.html', context)

    def post(self, request, *args, **kwargs):
        if self.kwargs['translatorCh'] == 'latinToCyrillic':
            fromL = 'Latin'
            toL = 'Cyrillic'
            self.result = translit(request.POST.get('text'), 'ru')

        elif self.kwargs['translatorCh'] == 'latinToGeorgian':
            fromL = 'Latin'
            toL = 'Georgian'
            self.result = translit(request.POST.get('text'), 'ka')

        elif self.kwargs['translatorCh'] == 'latinToArmenian':
            fromL = 'Latin'
            toL = 'Armenian'
            self.result = translit(request.POST.get('text'), 'hy')

        elif self.kwargs['translatorCh'] == 'latinToGreek':
            fromL = 'Latin'
            toL = 'Armenian'
            self.result = translit(request.POST.get('text'), 'el')

        elif self.kwargs['translatorCh'] == 'cyrillicToLatin':
            fromL = 'Cyrillic'
            toL = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'ru', reversed=True)

        elif self.kwargs['translatorCh'] == 'georgianToLatin':
            fromL = 'Georgian'
            toL = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'ka', reversed=True)

        elif self.kwargs['translatorCh'] == 'armenianToLatin':
            fromL = 'Armenian'
            toL = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'hy', reversed=True)

        elif self.kwargs['translatorCh'] == 'greekToLatin':
            fromL = 'Greek'
            toL = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'el', reversed=True)

        context = {
            'result': self.result,
            'fromL': fromL,
            'toL': toL
        }
        return render(request, 'translator.html', context)
