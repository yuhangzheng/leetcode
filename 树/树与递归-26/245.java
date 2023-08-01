/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// class Solution {
//     public int countNodes(TreeNode root) {
//         if (root == null) {
//             return 0;
//         }
        // int left = countNodes(root.left);
        // int right = countNodes(root.right);
        // return left + right + 1;

// }
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftH = 0;
        int rightH = 0;
        TreeNode n = root;
        while (n != null) {
            leftH += 1;
            n = n.left;
        }
        while (n!= null) {
            rightH += 1;
            n = n.right;
        }
        if (leftH == rightH) {
            return (int)Math.pow(2, leftH + 1) -1;
        }
        return countNodes(root.left) + countNodes(root.right) +1 ;
    }
}