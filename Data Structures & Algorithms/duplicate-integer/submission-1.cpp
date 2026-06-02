class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // std::unordered_map<int, int> freqs;

        // for (int num : nums) {
        //     freqs[num]++;
        // }

        // for (auto i : freqs) {
        //     if (i.second > 1) return true;
        // }

        // return false;

        std::unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                return true;
            }

            seen.insert(num);
        }

        return false;
    }
};