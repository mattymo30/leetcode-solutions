class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complements = new HashMap<>();

        int[] solution = new int[2];
        for (int i = 0; i < nums.length; i++){
            int value = nums[i];
            int comp = target - value;

            if(complements.containsKey(comp)) {
                solution[0] = (complements.get(comp));
                solution[1] = i;
                return solution;
            }

            complements.put(nums[i], i);
        }

        return null;
    }
}
