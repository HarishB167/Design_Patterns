from .task import Task

class TransferMoneyTask(Task):
    def _do_execute(self):
        print("Transfer Money")
