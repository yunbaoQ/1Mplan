#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

int ids_no_repeat_num(const vector<int>& ids){
    unordered_set<int> ids_memory;
    int num = 0;
    int i = 0;
    while(i < ids.size()){
        if (!ids_memory.count(ids[i])){
            ids_memory.insert(ids[i]);
            i++;
        }
        else{
            ids.erase(ids.begin() + i);
        }
    }
    num = ids.size();
    return(num);


}
int main(){
    vector<int> ids = { 1,1,2,3,4, };
	auto k = ids_no_repeat_num(ids);
	cout << k << endl;
	return(0);

}