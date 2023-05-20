package algorithms.sorting;

public abstract class Sort {

    public abstract int[] sort(int[] nums);

    /**
     * Swap the elements of index A and index B in an array and return the original array
     * @param indexA The first index for swapping
     * @param indexB The second index for swapping
     * @return The given array after swapping
     */
     public int[] swap(int[] nums, int indexA, int indexB) {
        int temp = nums[indexA];
        nums[indexA] = nums[indexB];
        nums[indexB] = temp;
        return nums;
    }

}
