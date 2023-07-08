from django.shortcuts import render

from .models import Question
import logging
logger = logging.getLogger('mysite')

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    logger.warning(
        'This is a warning!',
        exc_info=True
    )
    # ok
    return render(request, 'exemplo/index.html', context)
    # with error
    # return render(request, 'exemplo/views/index.html', context)