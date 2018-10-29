def min(arg, *args, value_to_key=None, **kwargs):
    if value_to_key is None:
        value_to_key = lambda x: x

    #в любом случае значение ключа заменится на х

    if len(args) > 0:
        values = args
        min_value, min_key = arg, value_to_key(arg)  #если есть аргумент, значит у него есть ключ
        #минимальное значение принимает нулевой позиционный аргумент, и минимальный ключ теперь его ключ
        has_initial_value = True
    #если позиционные переменные в картеже есть, то ее изначальное значение True,тк он не пуст

    else:
        values = arg
        min_value, min_key = None, None
        has_initial_value = False
     #наоборот, позиционных нет, потому и False, а раз нет ничего, то и значений None
    value_key_pairs = tuple(map(lambda x: (x, value_to_key(x)), values))
      #значения пар ключей представляются в виде картежа
    for value, key in value_key_pairs:
        if has_initial_value:
            if key < min_key:
                min_value, min_key = value, key
        #если ключ и значение в картеже, если есть аргументы, и ключ меньше минимального ключа, то минимальное значение и ключ
        #принимают значеня основных значения и ключа
        else:
            min_value, min_key = value, key
            has_initial_value = True

        # -//- ghbcdjbnm, даже если они не меньше, и заменить false на true, тк там уже не пусто

    if not has_initial_value:
        if 'default' in kwargs:
            return kwargs['default']
        raise ValueError('arg is an empty sequence')

        #если в словаре ничего нет значений, допустить ошибку значения, показать, что список пуст
    return min_value
        #вернуть минимальное значение, присвоенное самому маленькому значению

empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1

print(min(value_sequence))  # result: 1

print(min(x, y, z, value_to_key=lambda v: -v))  # result: 3
print(min(value_sequence, value_to_key=lambda v: -v))  # result: 3=

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599=E0F в шестнадцатиричной системе исчисления


print(min(empty_sequence))  # error!