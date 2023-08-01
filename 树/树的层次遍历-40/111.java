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
    public int minDepth(TreeNode root) {
        int ret = 0;
        if (root == null) {
            return ret;
        }
        Queue<TreeNode> que = new LinkedList<>();
        que.add(root);
        while (!que.isEmpty()){
            int n = que.size();
            ret++;
            System.out.println(n);
            for(int i = 0; i < n; i++) {
                TreeNode cur = que.poll();
                System.out.println(cur.val);
                if (cur.left != null) {
                    que.add(cur.left);
                }
                if (cur.right != null) {
                    que.add(cur.right);
                }
                if (cur.left == null && cur.right == null){
                    // System.out.println(cur.val);
                    return ret;
                }
            }
        }
        return ret;
    }
}