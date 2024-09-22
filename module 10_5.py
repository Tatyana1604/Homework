from threading import Thread
import datetime


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":   # снятие
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity


    def run(self, requests):
        th_list = []
        for request in requests:
            th = Thread(target=self.process_request, args=(request,))
            th.start()   # запуск потока
            th_list.append(th)

        for th in th_list:
            th.join()


if __name__ == '__main__':


    manager = WarehouseManager()

    # инициализация списка запросов
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50),

    ]

    start = datetime.datetime.now()
    manager.run(requests)
    end = datetime.datetime.now()
    print(manager.data)
    print(end-start)