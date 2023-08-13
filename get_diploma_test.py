# Дарья Можаева, 7-я когорта - Финальный проект. Инженер по тестированию плюс

import data as d
import sender_stand_request as s

# Создать заказ и получить трек заказа
def create_order():
    body = d.order_body.copy()
    print(body)
    response = s.request_create_order(d.headers, body)
    if response.status_code == 201:
        return response.json()["track"]
    else:
        print(f"[Ошибка] Получен статус {response.status_code}")


# Проверить, что код ответа равен 200
def check_status_code(response):
    assert response.status_code == 200, f"[Ошибка] Получен статус {response.status_code}"

# Выполнить запрос на получение заказа по треку
def get_order(track):
    order_param = d.param_order.copy()
    order_param["t"] = track
    response = s.request_get_order(order_param)
    check_status_code(response)
    return response

# Автоматизированный сценарий теста
def test_create_and_get_order():
    # Шаг 1: Создать заказ и получить трек заказа
    track = create_order()

    # Шаг 2: Выполнить запрос на получение заказа по треку заказа
    order_data = get_order(track)

    # Шаг 3: Проверить, что код ответа равен 200
    check_status_code(order_data)