from django.shortcuts import render
from django.http import HttpResponse

import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('Start page index')
    return HttpResponse("Привет МИР")


def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error to page: {e}')
        return HttpResponse('Oppss, karaul!!')
    else:
        logger.debug('Page about start')
        return HttpResponse("И тебе привет")

# Create your views here.
