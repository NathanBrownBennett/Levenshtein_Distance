def levenshtein_distance(s1, s2):
    if len(s1) == 0:
        return len(s2), ["Insert " + c for c in s2] 
    if len(s2) == 0:
        return len(s1), ["Delete " + c for c in s1]

    if s1[-1] == s2[-1]:
        cost = 0
        distance, edits = levenshtein_distance(s1[:-1], s2[:-1])
        return distance, edits  
    else:
        cost = 1
        distance_insert, edits_insert = levenshtein_distance(s1, s2[:-1])  
        distance_delete, edits_delete = levenshtein_distance(s1[:-1], s2)  
        distance_replace, edits_replace = levenshtein_distance(s1[:-1], s2[:-1]) 

        if distance_insert <= distance_delete and distance_insert <= distance_replace:
            edits_insert.append(f"Insert {s2[-1]}")
            return distance_insert + 1, edits_insert
        elif distance_delete <= distance_replace:
            edits_delete.append(f"Delete {s1[-1]}")
            return distance_delete + 1, edits_delete
        else:
            edits_replace.append(f"Substitute {s1[-1]} with {s2[-1]}")
            return distance_replace + cost, edits_replace

# Example usage:
distance, edits = levenshtein_distance("KU13043", "K2226138") 
print(distance)  # Output: 6
print(edits)  
