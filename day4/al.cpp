#include<iostream>
#include<unordered_map>

using namespace std;

vector<int> numRepeat(const vector<int>& ids){
    unordered_map<int, int> num_memory;
    vector<int> position = {};
    for(int i = 0; i < ids.size(); i++){
        num_memory[ids[i]]++;
    }
    for(int i = 0; i < ids.size(); i++){
        if(num_memory[ids[i]] == 1){
            position.push_back(i);
        }
    }
    if(position.size() == 0){
        position.push_back(-1);
    }

    return(position);


}
int main(){
    vector<int> ids = { 1,2,3,4,5 };
	auto k = numRepeat(ids);
	cout << "{";
    for (int i = 0; i < k.size(); i++){
        cout << k[i];
        if (i != k.size() - 1){
            cout << ",";
        }
    }
    cout << "}";
	return(0);

}