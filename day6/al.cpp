#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

int ids_no_repeat_num(vector<int>& ids) {
    unordered_set<int> ids_memory;
    int num = 0;
    int i = 0;
    int left = 0;
    while (i < ids.size()) {
        if (ids_memory.count(ids[i])) {
            i++;
        }
        else {
            ids_memory.insert(ids[i]);
            ids[left] = ids[i];
            i++;
            left++;
        }
    }
    num = left;
    return(num);


}
int main() {
    vector<int> ids = { 1,1,2,3,4, };
    auto k = ids_no_repeat_num(ids);
    cout << k << endl;
    cout << "[";
    for (int i = 0; i < k;i++) {
        cout << ids[i];
        if (i < k - 1) {
            cout << ",";
        }
    }
    cout << "]" << endl;
    return(0);

}