from books.Order import order


class order_auth:

 Orders_list:[order] = [
     order(1, 1/2/2022, 1, 1),
     order(2, 2/3/2022, 2, 2),
     order(3, 3/6/2022, 3, 3)]


def get_last_id_order(self):
    return self.Orders_list[len(self.Orders_list) - 1].get_id()