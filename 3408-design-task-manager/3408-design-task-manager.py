class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task = {task : (user, priority) for user, task, priority in tasks}
        self.heap = [(-priority, -task) for _, task, priority in tasks]
        heapify(self.heap)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task[taskId] = (userId, priority)
        heappush(self.heap, (-priority, -taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task[taskId] = (self.task[taskId][0], newPriority)
        heappush(self.heap, (-newPriority, -taskId))
        

    def rmv(self, taskId: int) -> None:
        del self.task[taskId]


    def execTop(self) -> int:
        while self.heap:
            priority, task_id = heappop(self.heap)
            if -task_id in self.task and self.task[-task_id][1] == -priority:
                user = self.task[-task_id][0]
                del self.task[-task_id]
                return user
        return -1