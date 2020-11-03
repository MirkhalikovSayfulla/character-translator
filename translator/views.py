from django.shortcuts import render
from transliterate import translit
from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class TranslateView(View):
    result = ''

    def get(self, request, *args, **kwargs):
        global from_l, to_l
        if self.kwargs['translatorType'] == 'latinToCyrillic':
            from_l = 'Latin'
            to_l = 'Cyrillic'

        elif self.kwargs['translatorType'] == 'latinToGeorgian':
            from_l = 'Latin'
            to_l = 'Georgian'

        elif self.kwargs['translatorType'] == 'latinToArmenian':
            from_l = 'Latin'
            to_l = 'Armenian'

        elif self.kwargs['translatorType'] == 'latinToGreek':
            from_l = 'Latin'
            to_l = 'Greek'

        elif self.kwargs['translatorType'] == 'cyrillicToLatin':
            from_l = 'Cyrillic'
            to_l = 'Latin'

        elif self.kwargs['translatorType'] == 'georgianToLatin':
            from_l = 'Georgian'
            to_l = 'Latin'

        elif self.kwargs['translatorType'] == 'armenianToLatin':
            from_l = 'Armenian'
            to_l = 'Latin'

        elif self.kwargs['translatorType'] == 'greekToLatin':
            from_l = 'Greek'
            to_l = 'Latin'

        context = {
            'result': self.result,
            'from_l': from_l,
            'to_l': to_l
        }
        return render(request, 'translator.html', context)

    def post(self, request, *args, **kwargs):
        global to_l, from_l
        if self.kwargs['translatorType'] == 'latinToCyrillic':
            from_l = 'Latin'
            to_l = 'Cyrillic'
            self.result = translit(request.POST.get('text'), 'ru')

        elif self.kwargs['translatorType'] == 'latinToGeorgian':
            from_l = 'Latin'
            to_l = 'Georgian'
            self.result = translit(request.POST.get('text'), 'ka')

        elif self.kwargs['translatorType'] == 'latinToArmenian':
            from_l = 'Latin'
            to_l = 'Armenian'
            self.result = translit(request.POST.get('text'), 'hy')

        elif self.kwargs['translatorType'] == 'latinToGreek':
            from_l = 'Latin'
            to_l = 'Armenian'
            self.result = translit(request.POST.get('text'), 'el')

        elif self.kwargs['translatorType'] == 'cyrillicToLatin':
            from_l = 'Cyrillic'
            to_l = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'ru', reversed=True)

        elif self.kwargs['translatorType'] == 'georgianToLatin':
            from_l = 'Georgian'
            to_l = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'ka', reversed=True)

        elif self.kwargs['translatorType'] == 'armenianToLatin':
            from_l = 'Armenian'
            to_l = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'hy', reversed=True)

        elif self.kwargs['translatorType'] == 'greekToLatin':
            from_l = 'Greek'
            to_l = 'Latin'
            self.result = translit(
                request.POST.get('text'), 'el', reversed=True)

        context = {
            'result': self.result,
            'from_l': from_l,
            'to_l': to_l
        }
        return render(request, 'translator.html', context)
