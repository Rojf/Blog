from marshmallow import Schema, fields, validate
from marshmallow.exceptions import ValidationError


class TagsField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return []
        if isinstance(value, list):
            return value
        return list(value.values_list('name', flat=True))


class AuthorSerializer(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    username = fields.String()


class PostSerializer(Schema):
    public_id = fields.Integer()
    title = fields.String(required=True, validate=validate.Length(min=10, max=250))
    slug = fields.String(validate=validate.Length(min=10, max=300))
    author = fields.Nested(AuthorSerializer())
    description = fields.String(required=True, validate=validate.Length(min=100, max=3000))
    tags = TagsField()

    # publish = fields.DateTime()
    publish = fields.String()
    created = fields.String()
    updated = fields.String()

    published = fields.Boolean()
    active = fields.Boolean()

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {'errors': err.messages}
        return data


class PostCreateOrUpdateSerializer(Schema):
    title = fields.String(required=True, validate=validate.Length(min=10, max=250))
    description = fields.String(required=True, validate=validate.Length(min=10, max=3000))
    tags = fields.List(fields.String())

    publish = fields.String()
    published = fields.Boolean()

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {'errors': err.messages}
        return data
