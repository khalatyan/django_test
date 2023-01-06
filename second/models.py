from django.db import models


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


class Lead(models.Model):
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
