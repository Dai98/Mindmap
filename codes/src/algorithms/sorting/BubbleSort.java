package algorithms.sorting;

import java.util.Arrays;

public class BubbleSort extends Sort{

    @Override
    public int[] sort(int[] nums) {
        boolean swapped = false;
        int n = nums.length;
        for(int k=n-1; k>0; k--) {
            for(int i=0; i<k; i++) {
                // Compare adjacent elements
                // If element on i is larger than i+1, swap i and i+1
                if (nums[i] > nums[i+1]) {
                    this.swap(nums, i, i+1);
                    swapped = true;
                }
            }

            // By now the largest element on 0...k is placed on k

            // If no swapping happens, then the array is already sorted
            // Sorting can be terminated
            if (!swapped) {
                break;
            }
        }

        return nums;
    }

    // Test
    public static void main(String[] args) {
        int[] nums = new int[] {1024, 5, 1, 23, 12, 77, 1010, -4, 1, 0, 76, 52};
        BubbleSort bubbleSort = new BubbleSort();
        System.out.println(Arrays.toString(bubbleSort.sort(nums)));
    }
}
