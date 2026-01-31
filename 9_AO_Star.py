# AO* algorithm code implementation (AND-OR graph search)
import heapq
from collections import defaultdict
from math import inf

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = self.h = self.f = 0
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.f < other.f
    def __repr__(self):
        return f"Node({self.name}, f={self.f})"

def heuristic(n):
    return {'A': 9, 'B': 6, 'C': 7, 'D': 3, 'E': 2, 'F': 0}.get(n, 999)

def aoStar(start, goal, graph):
    h = {n: heuristic(n) for n in graph}
    best_opt = {n: None for n in graph}
    solved, closed = set(), set()
    parents = defaultdict(set)
    open_list = [Node(start)]
    open_list[0].h, open_list[0].f = heuristic(start), heuristic(start)
    heapq.heapify(open_list)

    while open_list:
        cur = heapq.heappop(open_list)
        if cur.name in closed: continue
        opts = graph.get(cur.name, [])

        if not opts:
            if cur.name == goal:
                h[cur.name], solved.add(cur.name)
                for p in [x for x in parents[cur.name] if x in closed]:
                    closed.discard(p)
                    pn = Node(p)
                    pn.h, pn.f = h[p], h[p]
                    heapq.heappush(open_list, pn)
            else:
                h[cur.name] = inf
            closed.add(cur.name)
            continue

        best_cost, best = inf, None
        for opt in opts:
            cost = sum(w + h[c] for c, w in opt)
            if cost < best_cost:
                best_cost, best = cost, opt
            for c, _ in opt:
                parents[c].add(cur.name)

        h[cur.name], best_opt[cur.name] = best_cost, best
        if best and all(c in solved for c, _ in best):
            solved.add(cur.name)
            for p in [x for x in parents[cur.name] if x in closed]:
                closed.discard(p)
                pn = Node(p)
                pn.h, pn.f = h[p], h[p]
                heapq.heappush(open_list, pn)

        closed.add(cur.name)
        if best:
            for c, wt in best:
                if c not in closed and c not in solved:
                    cn = Node(c, cur.name)
                    cn.g, cn.h, cn.f = cur.g + wt, h[c], cur.g + wt + h[c]
                    heapq.heappush(open_list, cn)
                    print(f"  Added {c} to open list (f={cn.f})")

        if start in solved:
            print(f"\n START NODE '{start}' is SOLVED! ")
            break

    if start in solved:
        print(f"\n✓ Solution found! '{start}' can reach goal '{goal}'.")
        def rebuild(n, vis=None):
            vis = vis or set()
            if n in vis: return []
            vis.add(n)
            opt = best_opt.get(n)
            if not opt: return [(n, [])]
            res = [(n, [c for c, _ in opt])]
            for c, _ in opt:
                if c in solved:
                    res.extend(rebuild(c, vis))
            return res
        sol = rebuild(start)
        return (sol, h[start])
    return (None, None)
# Example AND-OR graph for AO* demonstration
# Format: node -> list of options (each option is a list of (child, cost) tuples)
# Example: 'A': [[('B', 2), ('C', 3)], [('D', 5)]] means:
#   - Option 1: Solve B AND C (both needed, costs 2 and 3)
#   - Option 2: Solve D alone (cost 5)

and_or_graph = {
    'A': [[('B', 2), ('C', 3)], [('D', 5)]],  # A: (B AND C) OR (D)
    'B': [[('E', 1)]],                          # B: E
    'C': [[('E', 2)]],                          # C: E
    'D': [[('F', 1)]],                          # D: F
    'E': [[('F', 1)]],                          # E: F
    'F': []                                     # F is goal (leaf/terminal)
}

if __name__ == '__main__':
    print("=" * 60)
    print("AO* Algorithm (AND-OR Graph Search)")
    print("=" * 60)
    print("\nSearching from 'A' to goal 'F'...")

    start = 'A'
    goal = 'F'
    result = aoStar(start, goal, and_or_graph)

    print("\n" + "=" * 60)
    if result[0]:
        solution, total_cost = result
        # Extract path from solution
        path = [node for node, _ in solution]
        path_str = " → ".join(path)
        print(f"Solution path: {path_str}")
        print(f"Total cost: {total_cost}")
    else:
        print("NO SOLUTION FOUND")
    print("=" * 60)