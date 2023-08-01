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
    // public int findSecondMinimumValue(TreeNode root) {
    //     int first, second = -1;
    //     Queue<TreeNode> que = new LinkedList<>();
    //     que.add(root);
    //     first = root.val;
    //     while (!que.isEmpty()) {
    //         TreeNode cur = que.poll();
    //         if (cur.val > first) {
    //             if (second == -1 || cur.val < second) {
    //                 second = cur.val;
    //             }
    //         }
    //         if (cur.left != null) {
    //             que.add(cur.left);
    //         }
    //         if (cur.right != null) {
    //             que.add(cur.right);
    //         }
    //     }
    //     return second;
    // }
    // dfs
    int first, second = -1;
    public int findSecondMinimumValue(TreeNode root) {
        first = root.val;
        second = -1;
        dfs(root);
        return second;
    }
    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        if (second != -1 && root.val >= second) {
            return;
        }
        if (root.val > first) {
            second = root.val;
        }
        dfs(root.left);
        dfs(root.right);
    }
}