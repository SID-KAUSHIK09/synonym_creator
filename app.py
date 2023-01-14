def synonym_creator(input):
    graph = {}
    for x in input:
        for phrase in x:
            if phrase not in graph:
                graph[phrase] = set(x.values())
            else:
                graph[phrase].update(x.values())
            for other_phrase in x.values():
                if other_phrase not in graph:
                    graph[other_phrase] = set(x.keys())
                else:
                    graph[other_phrase].update(x.keys())

    groups = []
    visited = set()
    for phrase in graph:
        if phrase not in visited:
            group = []
            dfs(phrase, graph, visited, group)
            groups.append(group)

    return groups

def dfs(phrase, graph, visited, group):
    visited.add(phrase)
    group.append(phrase)
    for other_phrase in graph[phrase]:
        if other_phrase not in visited:
            dfs(other_phrase, graph, visited, group)


input = [ {"Dg set": "Diesel generator"}, {"Organization": "Organisation"}, {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"} ]
print(synonym_creator(input))
