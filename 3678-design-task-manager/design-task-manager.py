class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskUser = {}
        self.taskPri = {} 
        self.ls = []

        for userId, taskId, priority in tasks :
            self.add(userId, taskId, priority)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskUser[taskId] = userId
        self.taskPri[taskId] = priority

        heapq.heappush(self.ls, (-priority, -taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskPri[taskId] = newPriority
        heapq.heappush(self.ls, (-newPriority, -taskId))
        

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskUser :
            del self.taskUser[taskId]
            del self.taskPri[taskId]

        

    def execTop(self) -> int:
        if not self.taskUser :
            return -1 
        while self.ls :
            priority, neg = heapq.heappop(self.ls)
            taskId = -neg 

            if taskId in self.taskPri and self.taskPri[taskId] == -priority :
                user = self.taskUser.pop(taskId)
                self.taskPri.pop(taskId)
                return user
        
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()