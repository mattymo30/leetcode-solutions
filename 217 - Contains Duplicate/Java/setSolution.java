class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<>();

        for (int num : nums) {
            if (visited.contains(num)){
                return true;
            }
            else{
                visited.add(num);
            }
        }
        return false;
    }
}
