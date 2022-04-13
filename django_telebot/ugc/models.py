from django.db import models


# Create your models here.
# id created by default
class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Внешний ID пользователя',
        unique=True,
    )
    name = models.TextField(
        verbose_name='Имя пользователя'
    )

    def __str__(self):
        return f'#{self.external_id} {self.name}'  # f-string

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(  # связь с внешней таблицей
        to='ugc.Profile',  # исключаем циклические импорты
        verbose_name='Профиль',
        on_delete=models.PROTECT,  # нельзя удалить профиль, к которому привязаны сообщения
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,  # время выставляет в момент сохранения нового объекта в базу силами Django
    )

    def __str__(self):  # красивое отображение
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'