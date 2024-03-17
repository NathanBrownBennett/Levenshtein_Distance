def levenshtein_distance(s1, s2):
    dp = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]
    changes = []
    total_cost = 0

    # Initialization to set cost for insertions/deletions
    for i in range(1, len(s1) + 1):
        dp[i][0] = i
    for j in range(1, len(s2) + 1):
        dp[0][j] = j  

    # Compare strings, character by character
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No change, cost = 0
            else:
                insert_cost = dp[i][j-1] + 1
                delete_cost = dp[i-1][j] + 1
                substitute_cost = dp[i-1][j-1] + 1

                dp[i][j] = min(insert_cost, delete_cost, substitute_cost)

    # Determine edits and calculate cost
    i, j = len(s1), len(s2)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1  
            total_cost += 0  # No change
        elif i > 0 and (j == 0 or dp[i - 1][j] <= dp[i][j - 1] and dp[i-1][j] <= dp[i-1][j-1]):
            changes.append(f"Delete {s1[i-1]} at position {i-1}, cost 1")
            i -= 1
            total_cost += 1
        elif j > 0 and (i == 0 or dp[i][j - 1] <= dp[i - 1][j] and dp[i][j-1] <= dp[i - 1][j - 1]):
            changes.append(f"Insert {s2[j-1]} at position {i-1}, cost 1")
            j -= 1
            total_cost += 1 
        else:
            changes.append(f"Substitute {s1[i-1]} with {s2[j-1]} at position {i-1}, cost 1")
            i -= 1
            j -= 1
            total_cost += 1

    return dp[-1][-1], dp, list(reversed(changes)), total_cost  

# Get the results from the function
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Get the results from the function
distance, table, edits, cost = levenshtein_distance(s1, s2) 

# Print the table with String A = s1 on the left and String B = s2 on the top
print("The table of distances is as follows:")

# Print header row
print(" ", end=" ")
for char in s2:
    print(char, end=" ")
print()

# Print the rest of the table
for i in range(len(s1)):
    print(s1[i], end=" ")
    for j in range(len(s2)):
        print(table[i + 1][j + 1], end=" ")  
    print()

# Print the rest of the output 
print(f"The Levenshtein distance is {distance}.")
print("The total cost of edits is: ", cost) 
print("The edits required are as follows:")
for edit in edits:
    print(edit)
