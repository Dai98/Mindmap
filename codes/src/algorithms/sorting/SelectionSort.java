package algorithms.sorting;

import util.SortTestManager;

import java.util.Arrays;

public class SelectionSort extends Sort{

    @Override
    public int[] sort(int[] nums) {
        // edge cases
        if (nums == null || nums.length < 2) {
            return nums;
        }

        int minIndex;

        for(int i=0; i<nums.length; i++) {
            minIndex = i;
            // Find the min(max) element in range k to n-1
            for(int k=i; k<nums.length; k++) {
                if (nums[k] < nums[minIndex]) {
                    minIndex = k;
                }
            }
            // Swap the element on index k with the min(max) element
            nums = this.swap(nums, minIndex, i);
        }

        return nums;
    }

    // Test
    public static void main(String[] args) {
        SortTestManager manager = new SortTestManager(50000, 1000, new SelectionSort());
        manager.test();
    }

}
