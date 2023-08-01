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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null) {
            return ret;
        }
        Queue<TreeNode> que = new LinkedList<>();
        que.add(root);
        while(!que.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int thisLevelSize = que.size();
            for (int i = 0; i < thisLevelSize; i++) {
                TreeNode p = que.poll();
                level.add(p.val);
                if (p.left != null) {
                    que.add(p.left);
                }
                if (p.right != null) {
                    que.add(p.right);
                }
            }
            ret.add(level);
        }
        return ret;        
    }
}