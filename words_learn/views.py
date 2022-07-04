from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from words_learn.models import Word
from django.db.models import Max

def learn(request):
    words = Word.objects.all()
    return HttpResponse(str(word.text + ' ' + word.translate + '</br>') for word in words)

def word(request, word_id):
    word = Word.objects.get(id=word_id)
    maxid = Word.objects.aggregate(Max('id'))['id__max']
    try:
        answer = request.POST['answer']
        if word.text == answer.lower():
            message = '回答正确'
        else:
            message = False
    except:
        message = ''

    return render(request, 'words_learn/words_learn.html', {
            'word':word, 
            'message': message,
            'nextid': word.id + 1 if word.id < maxid else word.id,
            'previd': word.id - 1 if word.id >= 2 else 1,
            })

    