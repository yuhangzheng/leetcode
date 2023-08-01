/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null) {
            return ret;
        }
        Queue<Node> que = new LinkedList<>();
        que.add(root);
        while(!que.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int thisLevelSize = que.size();
            for (int i = 0; i < thisLevelSize; i++) {
                Node p = que.poll();
                level.add(p.val);
                for (Node child : p.children) {
                    que.add(child);
                }
            }
            ret.add(level);
        }
        return ret;        
    }
}