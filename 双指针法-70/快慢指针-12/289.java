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
    public boolean isPalindrome(ListNode head) {
        ListNode mid = mid(head);
        ListNode h1 = head;  // 奇数多一个
        ListNode h2 = mid.next;
        h2 = reverseLink(h2);
        while (h2 != null) {
            if (h1.val != h2.val) {
                return false;
            }
            h2 = h2.next;
            h1 = h1.next;
        }
        return true;
    }
    public ListNode mid(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while(fast.next!= null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
    public ListNode reverseLink(ListNode head) {
        ListNode p = null;
        ListNode q = head;
        ListNode tmp = null;
        while(q != null) {
            tmp = q.next;
            q.next = p;
            p = q;
            q = tmp;
        }
        return p;
    }
}