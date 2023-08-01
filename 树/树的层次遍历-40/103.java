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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new LinkedList<List<Integer>>();
        if (root == null) {
            return ans;
        }
        boolean isLeft = true;
        Queue<TreeNode> que = new LinkedList<>();
        que.add(root);
        while (!que.isEmpty()) {
            Deque<Integer> levelList = new LinkedList<Integer>();
            int n = que.size();
            for (int i = 0; i < n; i++) {
                TreeNode cur = que.poll();
                if (isLeft) {
                    levelList.addLast(cur.val);                    
                }
                else {
                    levelList.addFirst(cur.val);
                }
                if (cur.left != null) {
                    que.add(cur.left);
                }
                if (cur.right != null) {
                    que.add(cur.right);
                }
            }
            isLeft = !isLeft;
            ans.add(new LinkedList<Integer>(levelList));
        }
        return ans;
    }
}