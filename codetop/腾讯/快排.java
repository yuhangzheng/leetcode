package codetop.腾讯;

class Solution {
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length-1);
        return nums;
    }
    public void quickSort(int[] nums, int l, int r) {
        if (l < r) {
            int pos = randomPartition(nums, l, r);
            quickSort(nums, l, pos-1);
            quickSort(nums, pos+1, r);
        }
    }
    public int randomPartition(int[] nums, int l, int r) {
        int i = new Random().nextInt(r-l+1) + l;
        swap(nums, r, i);
        return partition(nums, l, r);
    }
    public int partition(int[] nums, int l, int r) {        
        int pivot = nums[r];
        int i = l-1;
        for (int j = l; j <= r-1; j++) {
            if (nums[j] <= pivot) {
                i ++;
                swap(nums, i, j);
            }
        }
        swap(nums, i+1, r);
        return i+1;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}