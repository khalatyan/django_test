from django.db import models
from django.db.models.base import ModelBase


class MetaClass(ModelBase):

    # тут можно вызвать каую-то функцию внутри самого класс,
    # а можно оставить так, если для всех других классов логика
    # будет такая же
    def _get_state(cls, key):
        dict_key = "STATE_" + key.split("_")[1].upper()
        if dict_key in cls.STATES_DICT:
            def get_func():
                return cls.objects.filter(id=cls.STATES_DICT[dict_key])
            return get_func
        raise AttributeError(key)

    def __getattr__(cls, key):
        if key.startswith("get_"):
            return cls._get_state(key)
        raise AttributeError(key)


class DeliveryState(models.Model, metaclass=MetaClass):

    STATES_DICT = {
        "STATE_NEW": 1,  # Новая
        "STATE_ISSUED": 2,  # Выдана курьеру
        "STATE_DELIVERED": 3,  # Доставлена
        "STATE_HANDED": 4,  # Курьер сдал
        "STATE_REFUSED": 5,  # Отказ
        "STATE_PAID_REFUSED": 6,  # Отказ с оплатой курьеру
        "STATE_COMPLETE": 7,  # Завершена
        "STATE_NONE": 8  # Не определено
    }

    class Meta:
        verbose_name = u"Состояние доставки"
        verbose_name_plural = u"Состояния доставок"