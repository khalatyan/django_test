

@classmethod
# лучшк добавить декортатор @transaction.atomic
def buy(cls, user, item_id):
    product_qs = Product.objects.filter(item_id=item_id)

    # filter возвращает queryset или None, поэтому, можно проверку переписать
    # if product_qs:
    if product_qs.exists():
        # первый элемент можно получить через first()
        # product = product_qs.first()
        product = product_qs[0]

    if product.available:
        # product.available = False лучше сделать сразу после проверки
        # списание средств со счета пользователя
        # тут нет обработки ошибка, если вдруг метод не сможет списать средства со счета.
        # Если будет ошибка, нужно вернуть product.available = True
        user.withdraw(product.price)
        # информация о купленном товаре
        # информация о товаре не отправляется а метод, только о пользователе
        send_email_to_user_of_buy_product(user)
        product.available = False
        product.buyer = user
        product.save()
        return True
    else:
return False