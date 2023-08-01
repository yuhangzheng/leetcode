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
class Solution {
    int diameter = 0;
    // public int diameterOfBinaryTree(TreeNode root) {
    //     if (root == null) {
    //         return 0;
    //     }
    //     int cur = height(root.left) + height(root.right);
    //     int left = diameterOfBinaryTree(root.left);
    //     int right = diameterOfBinaryTree(root.right);
    //     int sub = left > right ? left : right;
    //     return cur > sub ? cur : sub; 
    // }

    // private int height(TreeNode root) {
    //     if (root == null) {
    //         return 0;
    //     }
    //     int left = height(root.left);
    //     int right = height(root.right);
    //     return left > right ? left + 1 : right + 1; 
    // }
    public int diameterOfBinaryTree(TreeNode root) {
        diameter = 1;
        depth(root);
        return diameter-1;
    }
    public int depth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = depth(root.left);
        int right = depth(root.right);
        diameter = Math.max(diameter, left + right + 1);
        return Math.max(left, right) + 1;
    }
}