from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse

from apps.notes.models import Note, WishList, NoteComment


# Create your views here.

def index(request):
    notes = Note.objects.all().order_by('-id')
    for note in notes:
        if request.user.is_authenticated:
            wish = WishList.objects.filter(user=request.user, note=note).first()
            if wish is not None:
                note.is_up = True
            else:
                note.is_up = False
        else:
            note.is_up = False
    return render(request, 'home.html', {"notes": notes})


def edit_note(request):
    return render(request, 'edit_note.html')


def detail(request, id):
    note = Note.objects.get(id=id)
    if request.user.is_authenticated:
        wish = WishList.objects.filter(user=request.user, note=note).first()
        if wish is not None:
            note.is_up = True
        else:
            note.is_up = False
    else:
        note.is_up = False
    return render(request, 'note.html', {'note': note})


@login_required
def store_note(request):
    note_pic = request.FILES.get('notePic')
    note_content = request.POST.get('noteContent')
    Note.objects.create(cover=note_pic, content=note_content, user=request.user)

    return HttpResponseRedirect('/')


@login_required
@csrf_exempt
def like_note(request):
    note_id = request.POST.get('id')
    note = Note.objects.get(id=note_id)
    wish_list = WishList.objects.filter(user=request.user, note=note).first()
    if wish_list is not None:
        wish_list.delete()
        result = 0
        note.unlike()
    else:
        WishList.objects.create(user=request.user, note=note).save()
        result = 1
        note.like()

    res = {
        "success": True,
        "result": result,
        "message": 'success'
    }

    return JsonResponse(res)


@login_required
def comment(request):
    comment = request.POST.get('comment')
    noteId = request.POST.get('noteId')
    note = Note.objects.get(id=noteId)
    NoteComment.objects.create(user=request.user, note=note, comment=comment)
    return HttpResponseRedirect('/note_detail/' + noteId)


@login_required
def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {"wishlist": wishlist})
