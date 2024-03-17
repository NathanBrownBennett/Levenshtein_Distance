def levenshtein_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    return min(levenshtein_distance(s1[:-1], s2) + 1,
               levenshtein_distance(s1, s2[:-1]) + 1,
               levenshtein_distance(s1[:-1], s2[:-1]) + cost)

# Example usage:
print(levenshtein_distance("kitten", "plum"))  # Output: 3
