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
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        int ret = root.val;
        que.add(root);
        while (!que.isEmpty()) {
            int n = que.size();
            for (int i = 0; i < n; i++) {
                TreeNode cur = que.poll();
                if (i == 0) {
                    ret = cur.val;
                }
                if (cur.left != null) {
                    que.add(cur.left);
                }
                if (cur.right!= null) {
                    que.add(cur.right);
                }
            }
        }
        return ret;
    }
}