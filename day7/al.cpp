#include<iostream>
#include<vector>

using namespace std;

int ids_no_repeat_num(vector<int>& ids) {
    int num = 0;
    int i = 1;
    int left = 1;
    while (i < ids.size()) {
        if (ids[i] == ids[i - 1]) {
            i++;
        }
        else {
            ids[left] = ids[i];
            i++;
            left++;
        }
    }
    num = left;
    return(num);


}
int main() {
    vector<int> ids = { 6,6,6 };
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