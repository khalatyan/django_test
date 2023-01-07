

@classmethod
# лучшк добавить декортатор @transaction.atomic
def buy(cls, user, item_id):
    # лучше сделать поиск сразу с использованием .first().
    # product = Product.objects.filter(item_id=item_id).first()
    product_qs = Product.objects.filter(item_id=item_id)

    # first() возвращает None или эл-т, поэтому проверку можно проести
    # if product:
    if product_qs.exists():
        product = product_qs[0]
    # Не указаны действия, если продукта не существует, это приведет к ошибке в следующем шаге

    if product.available:
        # product.available = False лучше сделать сразу после проверки
        # списание средств со счета пользователя
        # тут нет обработки ошибка, если вдруг метод не сможет списать средства со счета.
        # Если будет ошибка, нужно вернуть product.available = True
        user.withdraw(product.price)
        # информация о купленном товаре
        # информация о товаре не отправляется а метод, только о пользователе
        # такие действия можно выполнить в celery задачах, так как операция может быть долгая или
        # может вызвать ошибку
        send_email_to_user_of_buy_product(user)
        product.available = False
        product.buyer = user
        product.save()
        return True
    else:
        return False