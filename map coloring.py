def is_valid_assignment(assignments):
    for region, color in assignments.items():
        for neighbor in neighbors[region]:
            if assignments.get(neighbor) == color:
                return False
    return True

def map_coloring():
    regions = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS']
    colors = ['Red', 'Green', 'Blue']
    assignments = {}
    def backtrack(region_index):
        if region_index == len(regions):
            return True
        current_region = regions[region_index]
        for color in colors:
            assignments[current_region] = color
            if is_valid_assignment(assignments):
                if backtrack(region_index + 1):
                    return True
            del assignments[current_region]
        return False
    if backtrack(0):
        print("Solution found:")
        print(assignments)
    else:
        print("No solution exists.")
if __name__ == "__main__":
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'QLD'],
        'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
        'QLD': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'QLD', 'VIC'],
        'VIC': ['SA', 'NSW', 'TAS'],
        'TAS': ['VIC']
    }
    map_coloring()
