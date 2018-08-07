from uuid import uuid4

from django.db.models import (
    BinaryField,
    CharField,
    DateTimeField,
    Model,
    UUIDField,
)


class Resource(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    name = CharField(max_length=255)
    extension = CharField(max_length=255, blank=True)

    content = BinaryField()
    content_type = CharField(max_length=255)

    created_at = DateTimeField(auto_now_add=True)
