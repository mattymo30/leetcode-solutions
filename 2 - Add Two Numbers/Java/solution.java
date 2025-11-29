/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry_over = 0;
        ListNode temp = new ListNode();
        ListNode res = temp;

        while (l1 != null || l2 != null || carry_over == 1) {
            int total = 0;
            if (l1 != null) {
                total += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                total += l2.val;
                l2 = l2.next;
            }
            total += carry_over;
            carry_over = 0;

            if (total > 9) {
                carry_over = 1;
                total -= 10;
            }

            temp.next = new ListNode(total);
            temp = temp.next;
        }
        return res.next;
    }
}
