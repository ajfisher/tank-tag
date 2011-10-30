from django.shortcuts import get_object_or_404, render, redirect
from django.utils.html import strip_tags
from django_socketio import events

from tanks.models import Player

max_clients = 1

@events.on_message(channel="tank-play")
def play_message(request, socket, message):
    message = message[0]
    

@events.on_message(channel="tank")
def message(request, socket, message):
    socket.channels = ["tank-play"]
    message = message[0]
    if message["action"] == "mv":     
        # pick up the values from the socket message
        socket.broadcast_channel({"a": "ps", "x": message["ax"], "y": message["ay"], "pid": message["pid"]},
            channel="tank-play")

            
    if message["action"] == "fire":
        # send a fire broadcast
        socket.broadcast_channel({"a": "fire", "pid": message["pid"]},
            channel="tank-play")
        
    if message["action"] == "join":
        socket.channels = ["tank-play", "tank"]

        playername = strip_tags(message["username"])
                
        player, created = Player.objects.get_or_create(name=playername)
        
        if not created:
            socket.send({"a": "join_failed", "message": "name in use"})
        else:
            player.session = socket.session.session_id
            player.save()
            joined = {"a": "joined", "username": player.name, "id": player.id}
            socket.send(joined)
            socket.broadcast_channel(joined, channel="tank-play")

@events.on_disconnect(channel="tank")
def finish(request, socket):
    try:
        player = Player.objects.get(session=socket.session.session_id)
    except Player.DoesNotExist:
        return
    socket.broadcast_channel({"a": "leave", "username": player.name, "id": player.id}, channel="tank-play")
    player.delete()

def phonecontrol (request, template="tanks_client.html"):
    context = {}
    return render(request, template, context)
    
    
def showgame (request, template="tanks_play.html"):
    context = {}
    return render(request, template, context)
