def levenshtein_distance(s1, s2, show_trace=False):
    if len(s1) == 0:
        if show_trace: print(f"Returning {len(s2)}")
        return len(s2)
    if len(s2) == 0:
        if show_trace: print(f"Returning {len(s1)}")
        return len(s1)

    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    result =  min(levenshtein_distance(s1[:-1], s2, show_trace) + 1,
    levenshtein_distance(s1, s2[:-1], show_trace) + 1,
    levenshtein_distance(s1[:-1], s2[:-1], show_trace) + cost)

    if show_trace: 
        print(f"levenshtein_distance('{s1}', '{s2}') -> {result}") 
        return result

# Example usage with trace: 
print(levenshtein_distance("kitten", "sitting", show_trace=True))  

