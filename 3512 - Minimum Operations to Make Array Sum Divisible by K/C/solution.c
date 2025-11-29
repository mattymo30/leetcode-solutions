int minOperations(int* nums, int numsSize, int k) {
    int sum = 0;

    for (int i = 0; i < numsSize; i++) {
        int n = nums[i];
        sum += n;
    }

    return sum % k;
}
