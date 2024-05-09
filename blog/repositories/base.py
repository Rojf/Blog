from django.core.exceptions import ObjectDoesNotExist


class BaseRepository:
    model = None

    @classmethod
    def get(cls, *args, **kwargs):
        try:
            return cls.model.objects.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return

    @classmethod
    def create(cls, **kwargs):
        return cls.model.objects.create(**kwargs)

    @classmethod
    def update(cls, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def delete(cls, instance):
        instance.delete()

    @classmethod
    def all(cls, *args, **kwargs):
        return cls.model.objects.all(*args, **kwargs)
