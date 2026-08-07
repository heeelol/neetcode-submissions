class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;

        for (int i : nums) {
            if (seen.count(i) > 0) {
                return true;   
            }

            seen.insert(i);
        }

        return false;

    }
};