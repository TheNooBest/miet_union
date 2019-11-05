import vk  # Импортируем модуль vk

def vk_parse():

    def get_members(groupid):  # Функция формирования базы участников сообщества в виде списка
        first = vk_api.groups.getMembers(group_id=groupid, v=5.103)
        count = first["count"]
        return count

    token = "519f3103519f3103519f31034f51f283085519f519f31030c278301bba7a9674f4ec307"  # Сервисный ключ доступа
    session = vk.Session(access_token=token)  # Авторизация
    vk_api = vk.API(session)

    members = get_members(20030105)
    return members