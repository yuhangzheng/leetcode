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
    // public List<String> binaryTreePaths(TreeNode root) {
    //     List<String> paths = new ArrayList<>();
    //     constructPath(root, "", paths);
    //     return paths;
    // }
    // private void constructPath(TreeNode root, String path, List<String> paths) {
    //     if (root != null) {
    //         StringBuffer sb = new StringBuffer(path);
    //         sb.append(Integer.toString(root.val));
    //         if (root.left == null && root.right == null) {
    //             paths.add(sb.toString());
    //         }
    //         else {
    //             sb.append("->");
    //             constructPath(root.left, sb.toString(), paths);
    //             constructPath(root.right, sb.toString(), paths);
    //         }
    //     }
    // }
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<String>();
        if (root == null) {
            return paths;
        }
        Queue<TreeNode> nodeQueue = new LinkedList<TreeNode>();
        Queue<String> pathQueue = new LinkedList<String>();

        nodeQueue.add(root);
        pathQueue.add(Integer.toString(root.val));

        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.poll(); 
            String path = pathQueue.poll();

            if (node.left == null && node.right == null) {
                paths.add(path);
            } else {
                if (node.left != null) {
                    nodeQueue.add(node.left);
                    pathQueue.add(new StringBuffer(path).append("->").append(node.left.val).toString());
                }

                if (node.right != null) {
                    nodeQueue.add(node.right);
                    pathQueue.add(new StringBuffer(path).append("->").append(node.right.val).toString());
                }
            }
        }
        return paths;
    }

}