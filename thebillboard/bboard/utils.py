def floors():
    list1 = []
    for i in range(1, 21):
        list = []
        list.append(i)
        list.append(i)
        list = tuple(list)
        list1.append(list)
    list1 = tuple(list1)
    return list1

def rooms_amount():
    list1 = []
    for i in range(-1, 16):
        list = []
        list.append(i)
        list.append(str(i))
        list = tuple(list)
        list1.append(list)
    stud = (0, 'Студия')
    a = (None, 'Выбрать')
    list1[0] = a
    list1[1] = stud
    rooms_amount1 = tuple(list1)
    return rooms_amount1

rooms_amount1 = rooms_amount()

apartment_type_list = (('__empty__', 'Выбрать'), ('Квартира', 'Квартира'), ('Апартаменты', 'Апартаменты'),)
building_type_list = ((None, 'Выбрать'), ('Кирпичный', 'Кирпичный'), ('Блочный', 'Блочный'),
                      ('Монолитный', 'Монолитный'),('Панельный', 'Панельный'),
                      ('Монолитно-кирпичный', 'Монолитно-кирпичный'),)
parking_type_list = ((None, 'Выбрать'), ('Гараж', 'Гараж'), ('Машиноместо', 'Машиноместо'),)
old_new_list = ((None, 'Выбрать'), ('Новостройка', 'Новостройка'), ('Вторичный рынок', 'Вторичный рынок'),)
lift_amount = ((None, 'Выбрать'), (0, 'Отсутствует'), (1, '1'), (2, '2'), (3, '3'), (4, '4'),)
parking_adv_list = (('Подземная', 'Подземная'),
                    ('Наземная многоуровневая', 'Наземная многоуровневая'),('Открытая во дворе', 'Открытая во дворе'),
                    ('За шлагбаумом во дворе', 'За шлагбаумом во дворе'),)
action_list = (('buy_sell', 'Продать'), ('daily_rent', 'Сдать посуточно'), ('daily_rent', 'Сдать посуточно'),)
online_show_list = ((None, 'Выбрать'), ('Да', 'Да'), ('Нет', 'Нет'),)
