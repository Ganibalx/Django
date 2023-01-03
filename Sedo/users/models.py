from django.db import models  # Подключаем работу с моделями


# Создаем класс пользователей
class User(models.Model):
    userID = models.UUIDField(primary_key=True)
    userName = models.TextField()
    userSurname = models.TextField()
    userPatronymic = models.TextField()
    email = models.TextField()
    login = models.TextField()
    kode = models.TextField()

    def __str__(self):
        return self.userName, self.userSurname, self.userPatronymic


class Password(models.Model):
    userID = models.UUIDField(primary_key=True)
    userPass = models.TextField()

    def __str__(self):
        return self.userPass