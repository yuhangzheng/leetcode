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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null) {
            return false;
        }
        Queue<TreeNode> nodeQue = new LinkedList<>();
        Queue<Integer> valQue = new LinkedList<>();
        nodeQue.add(root);
        valQue.add(root.val);
        while(!nodeQue.isEmpty()) {
            TreeNode cur = nodeQue.poll();
            int curTotal = valQue.poll();
            if (cur.left == null && cur.right == null) {
                if (curTotal == targetSum) {
                    return true;
                }
                continue;
            }
            if (cur.left != null) {
                nodeQue.add(cur.left);
                valQue.add(curTotal + cur.left.val);
            }
            if (cur.right != null) {
                nodeQue.add(cur.right);
                valQue.add(curTotal + cur.right.val);
            }
        }
        return false;
    }
}