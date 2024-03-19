def levenshtein_distance(s1, s2, memo={}):
  """
  Calculates the Levenshtein distance between two strings using memoization.

  Args:
      s1: The first string.
      s2: The second string.
      memo: A dictionary to store previously calculated distances to reduce the amount of time processed and number of recursions.

  Returns:
      The Levenshtein distance between s1 and s2.
  """

  if len(s1) == 0:
    return len(s2)
  if len(s2) == 0:
    return len(s1)

  # Check if the distance for this substring pair is already calculated
  key = (len(s1), len(s2))
  if key in memo:
    return memo[key]

  # Calculate cost based on character similarity
  if s1[-1] == s2[-1]:
    cost = 0
  else:
    cost = 1

  # Recursively calculate distances for subproblems and store the result in memo
  memo[key] = min(levenshtein_distance(s1[:-1], s2, memo) + 1,
                   levenshtein_distance(s1, s2[:-1], memo) + 1,
                   levenshtein_distance(s1[:-1], s2[:-1], memo) + cost)

  return memo[key]

# Example usage
print(levenshtein_distance("KU13043", "K2273050"))  # Output: 3
