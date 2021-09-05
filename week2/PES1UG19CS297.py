"""
You can create any other helper funtions.
Do not modify the given functions
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def size(self):
        return len(self.stack)

    def pop(self):
        node = None
        if (self.size()):
            node = self.stack.pop()
        return node

class PQ_Node:
    def __init__(self, cost, node):
        self.cost = cost
        self.node = node

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        if self.cost > other.cost:
            return False
        return self.node < other.node

class Heap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        childpos = 2*pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def heappush(self, item):
        self.heap.append(item)
        self._siftdown(0, len(self.heap)-1)

    def heappop(self):
        last_element = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = last_element
            self._siftup(0)
            return returnitem
        return last_element


def findPath(parents, start, end):
    if start == end:
        return [start]
    path = [end]
    cur = end
    while not cur == start:
        cur = parents[cur]
        path.insert(0, cur)
    return path


def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    minCost = {start_point: 0}

    parents = [-1 for i in range(len(cost))]
    parents[start_point] = start_point

    pQueue = Heap()
    pQueue.heappush(PQ_Node(0, start_point))
    # pQueue = [PQ_Node(0, start_point)]
    visited = [False for i in range(len(cost))]

    while pQueue.size():

        # node = hq.heappop(pQueue).node
        node = pQueue.heappop().node

        if visited[node]:
            continue

        if node in goals:
            return findPath(parents, start_point, node)

        visited[node] = True

        for child in range(len(cost[node])):
            if cost[node][child] in [0, -1] or visited[child]:
                continue

            if child not in minCost or minCost[node] + cost[node][
                    child] <= minCost[child]:
                minCost[child] = minCost[node] + cost[node][child]
                parents[child] = node

            pQueue.heappush(PQ_Node(minCost[child] + heuristic[child], child))
    return []


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    path = []
    stack = Stack()
    stack.push(start_point)
    visited = [False for node in range(len(cost))]
    parents = [-1 for i in range(len(cost))]

    while stack.size():
        node = stack.pop()
        if node in goals:
            return findPath(parents, start_point, node)

        if visited[node]:
            continue

        visited[node] = True

        for child in range(len(cost[node]) - 1, 0, -1):
            if visited[child] == True or cost[node][child] in [0, -1]:
                continue
            stack.push(child)
            parents[child] = node
    return path
