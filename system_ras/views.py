from django.shortcuts import render
from .models import *
import asyncio
from django.http import StreamingHttpResponse
from ras import context_processors
from .services import *
from django.conf import settings
from django.http import request, HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    if 'create' in request.GET:
        if 'create_report' in request.GET['create']:
            response = create_report(request)
            return HttpResponse(json.dumps(response), content_type='application/json')
        if 'create_chart' in request.GET['create']:
            response = create_chart(request)
            return HttpResponse(json.dumps(response), content_type='application/json')

    return render(request, 'system_ras/index.html',
                  {
                      **context_processors.base(request),
                      'data_BLOCK_1': settings.DATA_BLOCK_1,
                      'data_BLOCK_2': settings.DATA_BLOCK_2,
                      'data_BLOCK_3': settings.DATA_BLOCK_3
                  })


async def sse_stream(request):
    """
    Sends server-sent events to the client.
    """

    async def event_stream():
        try:
            while True:
                yield f"data: {await get_data_ras()} \n\n"
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            raise

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
