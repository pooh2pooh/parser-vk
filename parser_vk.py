import vk  # Импортируем модуль vk


def get_members(groupid):
    first = vk_api.groups.getMembers(group_id=groupid, v=5.92)  # Первое выполнение метода
    data = first["items"]  # Присваиваем переменной первую тысячу id'шников
    count = first["count"] // 1000  # Присваиваем переменной количество тысяч участников
    # С каждым проходом цикла смещение offset увеличивается на тысячу
    # и еще тысяча id'шников добавляется к нашему списку.
    for i in range(1, count+1):  
        data = data + vk_api.groups.getMembers(group_id=groupid, v=5.92, offset=i*1000)["items"]
    return data


def save_data(data, filename="data.txt"):  # Функция сохранения базы в txt файле
    with open(filename, "w") as file:  # Открываем файл на запись
        # Записываем каждый id'шник в новой строке,
        # добавляя в начало "vk.com/id", а в конец перенос строки.
        for item in data:   
            file.write("vk.com/id" + str(item) + "\n") 


def enter_data(filename="data.txt"):  # Функция ввода базы из txt файла
    with open(filename) as file:  # Открываем файл на чтение
        b = [] 
        # Записываем каждую строчку файла в список,
        # убирая "vk.com/id" и "\n" с помощью среза.
        for line in file:   
            b.append(line[9:len(line) - 1])  
    return b


def get_intersection(group1, group2):
    group1 = set(group1)  
    group2 = set(group2)  
    intersection = group1.intersection(group2)  # Находим пересечение двух множеств
    all_members = len(group1) + len(group2) - len(intersection)  
    result = len(intersection)/all_members * 100  # Высчитываем пересечение в процентах
    print("Пересечение аудиторий: ", round(result,2), "%", sep="") 
    return list(intersection)


def union_members(group1, group2):
    group1 = set(group1)  
    group2 = set(group2)  
    union = group1.union(group2)  # Объединяем два множества
    return list(union) 


if __name__ == "__main__":
    token = ""  # Сервисный ключ доступа
    #session = vk.Session(access_token=token)  # Авторизация
    vk_api = vk.API(access_token=token)
    tester = get_members("poohprod")
    save_data(tester)
