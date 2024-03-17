import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LevenshteinDistance2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the first string: ");
        String s1 = scanner.nextLine();

        System.out.print("Enter the second string: ");
        String s2 = scanner.nextLine();

        scanner.close();

        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        List<String> changes = new ArrayList<>();
        int totalCost = 0;

        // Initialization to set cost for insertions/deletions
        for (int i = 1; i <= s1.length(); i++) {
            dp[i][0] = i;
        }
        for (int j = 1; j <= s2.length(); j++) {
            dp[0][j] = j;
        }

        // Compare strings, character by character
        for (int i = 1; i <= s1.length(); i++) {
            for (int j = 1; j <= s2.length(); j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1]; // No change, cost = 0
                } else {
                    int insertCost = dp[i][j - 1] + 1;
                    int deleteCost = dp[i - 1][j] + 1;
                    int substituteCost = dp[i - 1][j - 1] + 1;

                    dp[i][j] = Math.min(Math.min(insertCost, deleteCost), substituteCost);
                }
            }
        }

        // Determine edits and calculate cost
        int i = s1.length();
        int j = s2.length();
        while (i > 0 || j > 0) {
            if (i > 0 && j > 0 && s1.charAt(i - 1) == s2.charAt(j - 1)) {
                i--;
                j--;
                totalCost += 0; // No change
            } else if (i > 0 && (j == 0 || dp[i - 1][j] <= dp[i][j - 1] && dp[i - 1][j] <= dp[i - 1][j - 1])) {
                changes.add("Delete " + s1.charAt(i - 1) + " at position " + (i - 1) + ", cost 1");
                i--;
                totalCost += 1;
            } else if (j > 0 && (i == 0 || dp[i][j - 1] <= dp[i - 1][j] && dp[i][j - 1] <= dp[i - 1][j - 1])) {
                changes.add("Insert " + s2.charAt(j - 1) + " at position " + (i - 1) + ", cost 1");
                j--;
                totalCost += 1;
            } else {
                changes.add("Substitute " + s1.charAt(i - 1) + " with " + s2.charAt(j - 1) + " at position " + (i - 1) + ", cost 1");
                i--;
                j--;
                totalCost += 1;
            }
        }

        int distance = dp[s1.length()][s2.length()];
        int maxLen = Math.max(s1.length(), s2.length());
        double similarityScore = (double)(maxLen - distance) / maxLen;

        // Print the table with String A = s1 on the left and String B = s2 on the top
        System.out.println("The table of distances is as follows:");

        // Print header row
        System.out.print("  ");
        for (char c : s2.toCharArray()) {
            System.out.print(c + " ");
        }
        System.out.println();

        // Print the rest of the table
        for (i = 0; i < s1.length(); i++) {
            System.out.print(s1.charAt(i) + " ");
            for (j = 0; j < s2.length(); j++) {
                System.out.print(dp[i + 1][j + 1] + " ");
            }
            System.out.println();
        }

        // Print the rest of the output
        System.out.println("The Levenshtein distance is " + distance + ".");
        System.out.println("The total cost of edits is: " + totalCost);
        System.out.println("The edits required are as follows:");
        for (String edit : changes) {
            System.out.println(edit);
        }

        System.out.println("Similarity score: " + similarityScore);
    }
}