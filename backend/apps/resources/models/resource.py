from uuid import uuid4

from django.db.models import (
    BinaryField as _BinaryField,
    CharField,
    DateTimeField,
    Model,
    UUIDField,
)


class BinaryField(_BinaryField):

    def to_python(self, value):
        raise Exception([type(value), value])
        v = super().to_python(value)
        if isinstance(v, memoryview):
            return v.obj
        return v


class Resource(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    name = CharField(max_length=255)
    extension = CharField(max_length=255, blank=True)

    content = BinaryField()
    content_type = CharField(max_length=255)

    created_at = DateTimeField(auto_now_add=True)
