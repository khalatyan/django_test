from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Новый -> В работе
# В работе -> Приостановлен
# В работе -> Завершен
# Приостановлен -> В работе
# Приостановлен -> Завершен

class LeadState(models.Model):

    STATE_NEW = 1  # Новый
    STATE_IN_PROGRESS = 2  # В работе
    STATE_POSTPONED = 3  # Приостановлен
    STATE_DONE = 4  # Завершен

    name = models.CharField(
        u"Название",
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Lead(models.Model):

    STATUS_FLOW = {
        (LeadState.STATE_NEW, LeadState.STATE_IN_PROGRESS): ['send_mail', 'update_some_things'],
        (LeadState.STATE_IN_PROGRESS, LeadState.STATE_POSTPONED): ['update_some_things'],
        (LeadState.STATE_IN_PROGRESS, LeadState.STATE_DONE): ['send_mail'],
        (LeadState.STATE_POSTPONED, LeadState.STATE_IN_PROGRESS): [],
        (LeadState.STATE_POSTPONED, LeadState.STATE_DONE): ['change_fields'],
    }

    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name=u"Имя",
    )

    state = models.ForeignKey(
        LeadState,
        on_delete=models.PROTECT,
        default=LeadState.STATE_NEW,
        verbose_name=u"Состояние",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__old_state = self.state

    @classmethod
    def validate_state(self, old_state, new_state):
        # проверка на переход
        if (old_state.id, new_state.id) in Lead.STATUS_FLOW:
            # Возвращает методы, которые нужно вызвать
            return True
        else:
            raise ValidationError(
                _('Invalid transition: %(old_value)s -> %(new_value)s'),
                code='invalid',
                params={
                    'old_value': old_state.name,
                    'new_value': new_state.name,
                },
            )

    def save(self, *args, **kwargs):
        if not self.state == self.__old_state \
                and self.validate_state(self.__old_state, self.state):

            # Если переход статуса разрешается, вызываются методы
            funcs = Lead.STATUS_FLOW[(self.__old_state.id, self.state.id)]
            for func in funcs:
                getattr(self, func)()
            self.__old_state = self.state

        super(Lead, self).save(*args, **kwargs)


    # Примеры методов, которые вызываются при переходе статусов
    def send_mail(self):
        pass

    def change_fields(self):
        pass

    def update_some_things(self):
        pass


