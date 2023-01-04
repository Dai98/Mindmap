package util;
import java.util.Arrays;
import java.util.Random;
import algorithms.sorting.Sort;

public class SortTestManager extends TestManager{

    private final int testNum;
    private final int maxLength;
    private final Sort targetObject;

    public SortTestManager(int testNum, int maxLength, Sort sortObject) {
        this.testNum = testNum;
        this.targetObject = sortObject;
        this.maxLength = maxLength;
    }

    @Override
    public void test() {
        int failCount = 0;
        for(int i=1; i<=testNum; i++) {
            int[] nums1 = generateRandomArray();
            int[] nums2 = nums1.clone();

            // Conduct sorting
            nums1 = this.targetObject.sort(nums1);
            Arrays.sort(nums2);

            boolean result = isEqual(nums1, nums2);

            if (!result) {
                System.out.printf("Test %d failed\n", i);
                System.out.println("Sorting output:");
                System.out.println(Arrays.toString(nums1));
                System.out.println("Correct output:");
                System.out.println(Arrays.toString(nums2)+"\n");
                failCount++;
            }
        }

        System.out.println("All test cases are completed");
        if (failCount == 0) {
            System.out.println("No failed test case found");
        }
    }

    private int[] generateRandomArray() {
        Random random = new Random();
        int length = random.nextInt(this.maxLength);
        int[] array = new int[length];
        for(int i=0; i<length; i++) {
            array[i] = random.nextInt();
        }
        return array;
    }

    private boolean isEqual(int[] nums1, int[] nums2) {
        for(int i=0; i<nums1.length; i++) {
            if (nums1[i] != nums2[i]) {
                return false;
            }
        }
        return true;
    }
}
