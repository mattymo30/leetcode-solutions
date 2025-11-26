class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> parens = Map.of(
            ')', '(',
            '}', '{',
            ']', '['
        );

        String open_parens = "([{";
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (open_parens.contains(String.valueOf(c))) {
                stack.push(c);
            }
            else {
                if(stack.size() == 0) {
                    return false;
                }
                
                char paren_to_check = stack.pop();
                char close_paren = parens.get(c);

                if (close_paren != paren_to_check) {
                    return false;
                }
            }
        }
        if(stack.size() == 0) {
            return true;
        }
        return false;
    }
}
