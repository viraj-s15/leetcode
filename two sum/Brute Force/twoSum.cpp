
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output;
        for(auto it =  nums.begin(); it != nums.end(); it++) {
            auto it1 = find(it+1, nums.end(), target - *it);
            if(it1 != nums.end()) {
                output.push_back(it-nums.begin());
                output.push_back(it1-nums.begin());
        }
        }
        return output;
    }
};