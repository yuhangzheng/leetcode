package codetop.腾讯;

// class LRUCache extends LinkedHashMap<Integer, Integer> {
//     private int capacity;

//     public LRUCache(int capacity) {
//         super(capacity, 0.75F, true);
//         this.capacity = capacity;
//     }
    
//     public int get(int key) {
//         return super.getOrDefault(key, -1);
//     }
    
//     public void put(int key, int value) {
//         super.put(key, value);
//     }
//     @Override
//     protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
//         return size() > capacity; 
//     }

// }
class LRUCache {
    class LRULinkNode {
        int key;
        int value;
        LRULinkNode prev;
        LRULinkNode next;
        public LRULinkNode() {}
        public LRULinkNode(int _key, int _value) {
            key = _key;
            value = _value;
        }
    }
    private HashMap<Integer, LRULinkNode> cache = new HashMap();
    private int capacity;
    private int size;
    private LRULinkNode head, tail;

    public LRUCache(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        this.head = new LRULinkNode();
        this.tail = new LRULinkNode();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public int get(int key) {
        LRULinkNode node = this.cache.get(key);
        if (node == null) {
            return -1;
        }
        moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {
        LRULinkNode node = this.cache.get(key);
        if  (node == null) {
            LRULinkNode newNode = new LRULinkNode(key, value);
            cache.put(key, newNode);
            addToHead(newNode);
            size++;
            if (size > capacity) {
                LRULinkNode last = removeTail();
                cache.remove(last.key);
                size--;
            }
        }
        else {
            node.value = value;
            this.moveToHead(node);
        }
    }

    private void addToHead(LRULinkNode node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }
    private void removeNode(LRULinkNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    private void moveToHead(LRULinkNode node) {
        this.removeNode(node);
        this.addToHead(node);
    }
    private LRULinkNode removeTail() {
        LRULinkNode last = tail.prev;
        this.removeNode(last);
        return last;
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */