package algorithms.sorting;

import util.SortTestManager;

public class InsertionSort extends Sort {

    @Override
    public int[] sort(int[] nums) {
        // edge cases
        if (nums == null || nums.length < 2) {
            return nums;
        }

        for (int k=1; k<nums.length; k++) {
            // Element to be inserted is on index k
            for(int i=k; i>0; i--) {
                if (nums[i] < nums[i-1]) {
                    nums = this.swap(nums, i, i-1);
                } else {
                    // If not, then the element is on the correct position
                    // No need to iterate elements before current index
                    break;
                }
            }
        }

        return nums;
    }

    public static void main(String[] args) {
        SortTestManager manager = new SortTestManager(50000, 1000, new InsertionSort());
        manager.test();
    }
}
