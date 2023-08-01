/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        Map<Integer, Employee> map = new HashMap<>();
        for (Employee e : employees) {
            map.put(e.id, e);
        }

        int ret = 0;
        Queue<Integer> que = new LinkedList<>();
        que.add(id);
        while (!que.isEmpty()){
            int cur = que.poll();
            Employee curemp = map.get(cur);
            ret += curemp.importance;
            List<Integer> subor = curemp.subordinates;
            for (int e : subor) {
                que.add(e);
            }
        }
        return ret;
    }
}