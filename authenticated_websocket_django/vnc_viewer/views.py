from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from authenticated_websocket_django import settings


@login_required
def view_vnc_server(request):
    return render_to_response('vnc_viewer/vnc.html', {'STATIC_URL': settings.STATIC_URL})