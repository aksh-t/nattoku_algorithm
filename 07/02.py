graph = {}
graph["start"] = {}
graph["start"]["a"] = 10
graph["a"] = {}
graph["a"]["b"] = 20
graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30
graph["c"] = {}
graph["c"]["a"] = 1
graph["fin"] = {}

costs = {n: c for n, c in graph["start"].items()} | {"fin": float("inf")}
parents = {n: "start" for n in graph["start"].keys()} | {"fin": None}
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
while node:
    for n, c in graph[node].items():
        if n not in costs or costs[n] > costs[node] + c:
            costs[n] = costs[node] + c
            parents[n] = node
    processed += [node]
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
