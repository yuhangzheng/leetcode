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
    List<List<Integer>> ret = new LinkedList<List<Integer>>();
    Map<TreeNode, TreeNode> map = new HashMap<TreeNode, TreeNode>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if(root == null) {
            return ret;
        }

        Queue<TreeNode> nodeQue = new LinkedList<>();
        Queue<Integer> valQue = new LinkedList<>();
        nodeQue.add(root);
        valQue.add(0);
        while(!nodeQue.isEmpty()) {
            TreeNode cur = nodeQue.poll();
            int curTotal = valQue.poll() + cur.val;
            if (cur.left == null && cur.right == null) {
                if (curTotal == targetSum) {
                    getPath(cur);
                }
                continue;
            }
            if (cur.left != null) {
                map.put(cur.left, cur);
                nodeQue.add(cur.left);
                valQue.add(curTotal);
            }
            if (cur.right != null) {
                map.put(cur.right, cur);
                nodeQue.add(cur.right);
                valQue.add(curTotal);
            }
        }
        return ret;
    }
    private void getPath(TreeNode node) {
        List<Integer> tmp = new ArrayList<>();
        while (node != null) {
            tmp.add(node.val);
            node = map.get(node);
        }
        Collections.reverse(tmp);
        ret.add(new ArrayList<Integer>(tmp));
    }
}