class Solution {
    public int findDuplicate(int[] nums) {
        // int n = nums.length;
        // int l = 1, r = n - 1, ans = -1;
        // while(l <= r) {
        //     int mid = (l + r) / 2 ;
        //     int cnt = 0;
        //     for (int i = 0; i < n; i ++) {
        //         if (nums[i] <= mid) {
        //             cnt += 1;
        //         }
        //     }
        //     if (cnt <= mid) {
        //         l = mid + 1;
        //     }
        //     else {
        //         r = mid - 1;
        //         ans = mid;
        //     }
        // }
        // return ans;
        int slow = 0, fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = 0;
        while (fast != slow) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    
    }
}