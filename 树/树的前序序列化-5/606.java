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
//     public String tree2str(TreeNode root) {
//         StringBuffer sb = new StringBuffer();
//         pre(root, sb);
//         return sb.toString();
//     }
//     private void pre(TreeNode root, StringBuffer sb) {
//         if (root == null) {
//             return;
//         }
//         sb.append(root.val);
//         if (root.left == null && root.right == null) {
//             return;
//         }
//         sb.append("(");
//         pre(root.left, sb);
//         sb.append(")");
//         if (root.right != null) {
//             sb.append("(");
//             pre(root.right, sb);
//             sb.append(")");
//         }
//     }
// }
class Solution {
    public String tree2str(TreeNode root) {
        if (root == null) {
            return "";
        }
        if (root.left == null && root.right == null) {
            return Integer.toString(root.val);
        }
        if (root.right == null) {
            return new StringBuffer().append(root.val).append("(").append(tree2str(root.left)).append(")").toString();
        }
        return new StringBuffer().append(root.val).append("(").append(tree2str(root.left)).append(")(").append(tree2str(root.right)).append(")").toString();
    }
}