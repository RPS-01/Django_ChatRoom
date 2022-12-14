from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
def index_view(request):
    return render(request, "chat/index.html", {})

@login_required
def room_view(request, room_name):

    return render(
        request,
        "chat/chatroom.html",
        {
            "room_name_json": mark_safe(json.dumps(room_name)),
            "username": mark_safe(json.dumps(request.user.username)),
        }
    )
