class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> freqs;

        for (int num : nums) {
            freqs[num]++;
        }

        for (auto i : freqs) {
            if (i.second > 1) return true;
        }
        return false;
    }
};