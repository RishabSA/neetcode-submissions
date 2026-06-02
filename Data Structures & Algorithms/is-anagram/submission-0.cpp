class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> freqs;

        for (char c : s) {
            freqs[c]++;
        }

        for (char c : t) {
            freqs[c]--;
        }

        for (auto i : freqs) {
            if (i.second != 0) return false;
        }
        return true;
    }
};
