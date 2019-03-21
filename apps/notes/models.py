from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.accounts.models import UserAccount


# Create your models here.
class Note(models.Model):
    content = models.CharField(max_length=800, verbose_name="content", default='')
    cover = models.ImageField(upload_to="image/%Y/%m", max_length=100, default='')
    tag = models.CharField(max_length=256, null=True, verbose_name='tags')
    like_count = models.IntegerField(default=0, verbose_name='like_count')
    user = models.ForeignKey(UserAccount, to_field='id', default=0, on_delete=True, verbose_name="user_id")
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "note"

    def __unicode__(self):
        return self.content

    def like(self):
        self.like_count += 1
        self.save()

    def unlike(self):
        self.like_count -= 1
        self.save()

    def comment_list(self):
        comments = NoteComment.objects.filter(note=self)
        return comments


class NoteComment(models.Model):
    user = models.ForeignKey(UserAccount, to_field='id', default=0, on_delete=True, verbose_name="user_id")
    note = models.ForeignKey(Note, verbose_name="note_id", on_delete=True)
    comment = models.CharField(max_length=300, verbose_name="comment")
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "comment"


class WishList(models.Model):
    user = models.ForeignKey(UserAccount, to_field='id', default=0, on_delete=True, verbose_name="user_id")
    note = models.ForeignKey(Note, verbose_name="note_id", on_delete=True)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "wishlist"
