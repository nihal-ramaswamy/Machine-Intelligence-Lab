"""
You can create any other helper funtions.
Do not modify the given functions
"""


class Stack:
    def __init__(self, root):
        self.stack = [root]

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

    def __repr__(self):
        print(f"Node: {self.node} Cost: {self.cost}")


class Heap:
    def __init__(self, root):
        self.heap = [root]

    def _siftup(self, pos):
        end = self.size()
        start = pos
        newitem = self.heap[pos]
        child = 2 * pos + 1
        while child < end:
            right = child + 1
            if right < end and not self.heap[child] < self.heap[right]:
                child = right
            self.heap[pos] = self.heap[child]
            pos = child
            child = 2 * pos + 1
        self.heap[pos] = newitem
        self._siftdown(start, pos)

    def _siftdown(self, start, pos):
        newitem = self.heap[pos]
        while pos > start:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def size(self):
        return len(self.heap)

    def heappush(self, item):
        self.heap.append(item)
        self._siftdown(0, len(self.heap) - 1)

    def heappop(self):
        last_element = self.heap.pop()
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = last_element
            self._siftup(0)
            return returnitem
        return last_element


def getCommonVars(length, start, root, data_structure):
    visited = [False] * length
    parents = [-1] * length
    parents[start] = start
    if data_structure == "Heap":
        return [visited, parents, Heap(root)]
    else:
        return [visited, parents, Stack(root)]


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
    visited, parents, pQueue = getCommonVars(len(cost), start_point,
                                             PQ_Node(0, start_point), "Heap")
    while pQueue.size():
        node = pQueue.heappop().node
        if visited[node]:
            continue
        if node in goals:
            return findPath(parents, start_point, node)
        visited[node] = True
        for child in range(len(cost[node])):
            if cost[node][child] in [0, -1] or visited[child]:
                continue
            child_cost = minCost[node] + cost[node][child]
            if child not in minCost or child_cost <= minCost[child]:
                minCost[child] = child_cost
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
    visited, parents, stack = getCommonVars(len(cost), start_point,
                                            start_point, "Stack")
    while stack.size():
        node = stack.pop()
        if node in goals:
            return findPath(parents, start_point, node)
        if visited[node]:
            continue
        visited[node] = True
        for child in range(len(cost[node]) - 1, 0, -1):
            if visited[child] or cost[node][child] in [0, -1]:
                continue
            stack.push(child)
            parents[child] = node
    return []
