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
    HashMap<Integer, Integer> map = new HashMap();
    public int[] findFrequentTreeSum(TreeNode root) {
        ArrayList <Integer> res = new ArrayList();
        int maxcnt = 0;
        subTree(root);
        for (Map.Entry <Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > maxcnt) {
                res.clear();
                res.add(entry.getKey());
                maxcnt = entry.getValue();
            }
            else if (entry.getValue() == maxcnt) {
                res.add(entry.getKey());
            }
        }
        int[] ans = new int[res.size()];
        for (int i = 0; i < res.size(); ++i) {
            ans[i] = res.get(i);
        }
        return ans;
    }
    private int subTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int res = root.val + subTree(root.left) + subTree(root.right);
        if (map.containsKey(res)) {
            map.put(res, map.get(res) + 1);
        }
        else {
            map.put(res, 1);
        }
        // 便捷写法
        // cnt.put(sum, cnt.getOrDefault(sum, 0) + 1);
        return res;
    }
}