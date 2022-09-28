from django.shortcuts import render
from django.http import JsonResponse
import ast



from . import forms
from . import poetry_extractor

def home(request):
    form = forms.MainForm()

    if request.method == 'POST':
        form = forms.MainForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'core/index.html', 
    {'form': form})

def get_poem(request):
    if request.method == "POST":
        # convert bytes to dict
        data = ast.literal_eval(request.body.decode('utf-8'))
        author_name = data['myData']

        # get title of some poem
        p_e = poetry_extractor.PoetryExtractor()
        p_e.url =  "https://poetrydb.org/author/{}/title".format(str(author_name))

        title = p_e.get_random_work()

        # get text of the title selected previously
        p_e.url = "https://poetrydb.org/author,title/{};{}".format(author_name, title['title'])

        text = p_e.get_data()

        data = {
            'title':title,
            'text': text,
        }
        return JsonResponse(data)
    else:
        data = {
            "msg": "It worked!!",
        }
        return JsonResponse(data)

    

   