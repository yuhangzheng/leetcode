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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) {
            return;
        }
        ListNode mid = mid(head);
        ListNode h1 = head;
        ListNode h2 = mid.next;
        mid.next = null;
        h2 = reverseLink(h2);
        mergeLink(h1,h2);

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

    public void mergeLink(ListNode h1, ListNode h2) {
        ListNode p1;
        ListNode p2;
        while (h1 != null && h2 != null) {
            p1 = h1.next;
            p2 = h2.next;

            h1.next = h2;
            h1 = p1;
            
            h2.next = h1;
            h2 = p2;
        }
    }
}