#include <iostream>
#include <string>

using namespace std;

int levenshteinDistance(const string& s1, const string& s2) {
    if (s1.empty()) {
        return s2.length();
    }

    if (s2.empty()) {
        return s1.length();
    }

    int cost = (s1.back() == s2.back()) ? 0 : 1;

    return min({levenshteinDistance(s1.substr(0, s1.length() - 1), s2) + 1,
                levenshteinDistance(s1, s2.substr(0, s2.length() - 1)) + 1,
                levenshteinDistance(s1.substr(0, s1.length() - 1),
                                    s2.substr(0, s2.length() - 1)) + cost});
}

int main() {
    string s1 = "kitten";
    string s2 = "sitting";
    cout << levenshteinDistance(s1, s2) << endl; // Output: 3
    return 0;
}
