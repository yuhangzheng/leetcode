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
    public int maxDepth(Node root) {
        int ret = 0;
        if (root == null) {
            return ret;
        }
        Queue<Node> que = new LinkedList<>();
        que.add(root);
        while(!que.isEmpty()) {
            int n = que.size();
            while (n > 0) {
                Node cur = que.poll();
                for (Node node : cur.children) {
                    que.add(node);
                }
                n --;  
            }
            ret ++;
        }
        return ret;
    }
}