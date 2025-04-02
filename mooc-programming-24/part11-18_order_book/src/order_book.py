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
            print(order.id == id)
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
        

    