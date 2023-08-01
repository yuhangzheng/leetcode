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
    // dfs
    // List<Integer> allNum = new ArrayList<>(); 
    // public int sumNumbers(TreeNode root) {
    //     dfs(root, 0);
    //     int sum = 0;
    //     for (int i : allNum) {
    //         sum += i;
    //     }
    //     return sum;
    // }
    // private int dfs(TreeNode root, int cur) {
    //     cur = cur * 10 + root.val;
    //     if (root.left == null && root.right == null) {
    //         allNum.add(cur);
    //         return cur;
    //     }
    //     if (root.left != null){
    //         dfs(root.left, cur);
    //     }
    //     if (root.right != null) {
    //         dfs(root.right, cur);
    //     }
    //     return cur;
    // }
    public int sumNumbers(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int sum = 0;
        Queue<TreeNode> nodeQueue = new LinkedList<TreeNode>();
        Queue<Integer> numQueue = new LinkedList<Integer>();
        nodeQueue.add(root);
        numQueue.add(root.val);
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.poll();
            int num = numQueue.poll();
            TreeNode left = node.left, right = node.right;
            if (left == null && right == null) {
                sum += num;
            } else {
                if (left != null) {
                    nodeQueue.add(left);
                    numQueue.add(num * 10 + left.val);
                }
                if (right != null) {
                    nodeQueue.add(right);
                    numQueue.add(num * 10 + right.val);
                }
            }
        }
        return sum;
    }
}