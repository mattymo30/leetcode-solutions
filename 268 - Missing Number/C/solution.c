int missingNumber(int* nums, int numsSize) {
    int temp[numsSize + 1];

    for (int i = 0; i < numsSize + 1; i++) {
        temp[i] = -1;
    }

    for (int i = 0; i < numsSize; i++) {
        int n = nums[i];
        temp[n] = 1;
    }

    for (int i = 0; i < numsSize + 1; i++) {
        int n = temp[i];
        if (n == -1) {
            return i;
        }
    }

    return 0;
}
