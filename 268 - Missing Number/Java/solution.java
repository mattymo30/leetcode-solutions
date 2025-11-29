class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;

        int[] temp = new int[n + 1];

        for (int i = 0; i < n + 1; i++) {
            temp[i] = -1;
        }

        for (int num : nums) {
            temp[num] = 1;
        }

        for (int i = 0; i < n + 1; i++) {
            int num = temp[i];
            if (num == -1) {
                return i;
            }
        }

        return 0;
    }
}
