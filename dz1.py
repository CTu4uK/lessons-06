# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.


from time import sleep
from datetime import datetime as dt


class TrafficLight:

    _states = {"Красный": 7, "Жёлтый": 2, "Зелёный": 10}
    _color = ''

    def running(self):

        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"TrafficLight перешел в состояние '{self._color}' "
                  f"на {sw_time} секунд")

            sleep(sw_time)

            print(f"TrafficLight перешел в состояние '{self._color}' после " 
                  f"{(dt.now() - start_state_time).seconds} секунд")

tl = TrafficLight()
tl.running()
