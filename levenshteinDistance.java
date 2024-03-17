public class levenshteinDistance {

  public static int levenshteinDistance(String s1, String s2) {
      if (s1.isEmpty()) {
          return s2.length();
      }

      if (s2.isEmpty()) {
          return s1.length();
      }

      int cost = (s1.charAt(s1.length() - 1) == s2.charAt(s2.length() - 1)) ? 0 : 1;

      return Math.min(
              Math.min(
                 levenshteinDistance(s1.substring(0, s1.length()-1),s2) + 1,
                 levenshteinDistance(s1,s2.substring(0, s2.length()-1)) + 1),
                 levenshteinDistance(s1.substring(0,s1.length()-1),
                                     s2.substring(0,s2.length()-1)) + cost
        );
    }

    public static void main(String[] args) {
        String s1 = "kitten";
        String s2 = "sitting";
        System.out.println(levenshteinDistance(s1, s2)); // Output: 3
    }
}
