package algorithms.sorting;

import util.SortTestManager;

import java.util.Arrays;

public class MergeSort extends Sort{

    @Override
    public int[] sort(int[] nums) {
        // edge cases
        if (nums == null || nums.length < 2) {
            return nums;
        }

        nums = sortRecur(nums, 0, nums.length-1);

        return nums;
    }

    public int[] sortRecur(int[] nums, int left, int right) {
        if (left == right) {
            return nums;
        }

        // middle point of left and right
        int mid = left + (right - left)/2;

        // Recursively keep left and right half sorted
        int[] leftSorted = sortRecur(nums, left, mid);
        int[] rightSorted = sortRecur(nums, mid+1, right);

        // temp space
        int[] temp = new int[nums.length];
        int tempIndex = left;

        // Merge
        int p1 = left;
        int p2 = mid+1;

        // During merge, when the left half and the right half all have elements to be put in the temp space
        while (p1 <= mid && p2 <= right) {
            if (leftSorted[p1] > rightSorted[p2]) {
                temp[tempIndex++] = rightSorted[p2++];
            } else {
                temp[tempIndex++] = leftSorted[p1++];
            }
        }

        // When left half still has elements to be put in the temp space
        while (p1 <= mid) {
            temp[tempIndex++] = leftSorted[p1++];
        }

        // When right half still has elements to be put in the temp space
        while (p2 <= right) {
            temp[tempIndex++] = rightSorted[p2++];
        }

        // Copy the sorted area in temp space to the original array
        if (right + 1 - left >= 0) {
            System.arraycopy(temp, left, nums, left, right + 1 - left);
        }

        return nums;
    }

    public static void main(String[] args) {
        SortTestManager manager = new SortTestManager(50000, 1000, new MergeSort());
        manager.test();
    }
}
