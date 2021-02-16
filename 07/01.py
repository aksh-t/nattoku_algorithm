graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"] = {}
graph["d"]["fin"] = 1
graph["fin"] = {}

costs = {n: w for n, w in graph["start"].items()}
costs |= {"fin": float("inf")}

parents: dict[str, str] = {n: "start" for n in graph["start"].keys()}
parents |= {"fin": None}

processed = []


def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_cost_node = None

    for n, c in costs.items():
        if lowest_cost > c and n not in processed:
            lowest_cost = c
            lowest_cost_node = n
    return lowest_cost_node


node = find_lowest_cost_node()
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = costs[node] + cost
        if n not in costs or costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node()

print(costs)
print(parents)
print(processed)

print(f"lowest_cost: {costs['fin']}")

node = "fin"
route = [node]
while node != "start":
    node = parents[node]
    route += [node]
print(f"route: {route[::-1]}")
