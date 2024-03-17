def levenshtein_distance(s1, s2):
    dp = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])      # Replace

    # save changes
    changes = []
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i-1][j-1] + 1:
                changes.append(f"Substitute {s1[i-1]} with {s2[j-1]} at position {i-1}, cost 1")
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i-1][j] + 1:
                changes.append(f"Delete {s1[i-1]} at position {i-1}, cost 1")
                i -= 1
            elif dp[i][j] == dp[i][j-1] + 1:
                changes.append(f"Insert {s2[j-1]} at position {j-1}, cost 1")
                j -= 1

    while i > 0:
        changes.append(f"Delete {s1[i-1]} at position {i-1}, cost 1")
        i -= 1
    while j > 0:
        changes.append(f"Insert {s2[j-1]} at position {j-1}, cost 1")
        j -= 1

    return dp[-1][-1], dp, list(reversed(changes))

# Usage example:
distance, table, edits = levenshtein_distance("PLUM", "PEAR")

print(f"The Levenshtein distance is {distance}.")
print("The table of distances is as follows:")
for row in table:
    print(row)
print("The edits required are as follows:")
for edit in edits:
    print(edit)
