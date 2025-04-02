class Task:
    id = 1
    def __init__(self, description: str, programmer: str, workload: int) -> None:
        self.id = Task.id
        Task.id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
    
    def finished_or_not(self) -> str:
        return "FINISHED" if self.finished else "NOT FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished_or_not()}"

    def is_finished(self) -> bool:
        return self.finished
    
    def mark_finished(self):
        self.finished = True
    
class OrderBook: 
    def __init__(self):
        self.orders = []
        self.programmers_set = set()

    def add_order(self, description: str, programmer: str, workload: int):
        order = Task(description, programmer, workload)
        self.orders.append(order)
        self.programmers_set.add(programmer)
    
    def all_orders(self) -> list:
        return self.orders
    
    def programmers(self):
        return list(self.programmers_set)

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError(f"Order with id {id} does not exists!")
    
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str) -> tuple:
        finished = 0
        unfinished = 0
        finished_hours = 0
        unfinished_hours = 0
        if programmer not in self.programmers_set:
            raise ValueError("No programmer with such name!")
        for order in self.finished_orders():
            if order.programmer == programmer:
                finished += 1
                finished_hours += order.workload
        for order in self.unfinished_orders():
            if order.programmer == programmer:
                unfinished += 1
                unfinished_hours += order.workload
        return (finished, unfinished, finished_hours, unfinished_hours)

class Application:
    def __init__(self):
        self.orderbook = OrderBook()
    
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def add_order(self):
        description = input("description: ")
        rest = input("programmer and workload estimate: ")
        try:
            programmer = rest.split(" ")[0]
            workload = int(rest.split(" ")[-1])
            self.orderbook.add_order(description, programmer, workload)
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished_tasks(self):
        if len (self.orderbook.finished_orders()) == 0:
            print("no finished tasks")
        else:
            for order in self.orderbook.finished_orders():
                print(order)

    def list_unfinished_tasks(self):
        if len (self.orderbook.unfinished_orders()) == 0:
            print("no unfinished tasks")
        else:
            for order in self.orderbook.unfinished_orders():
                print(order)
    
    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.orderbook.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def programmers(self):
        for programmer in list(self.orderbook.programmers_set):
            print(programmer)

    def status(self):
        try:
            programmer = input("programmer: ")
            programmer_data = self.orderbook.status_of_programmer(programmer)
            print(f"tasks: finished {programmer_data[0]} not finished {programmer_data[1]}, hours: done {programmer_data[2]} scheduled {programmer_data[3]}")
        except ValueError:
                print("erroneous input")

    def execute(self):
        self.help()
        print("")
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status()
            else:
                self.help()         

Application().execute()