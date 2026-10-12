#include<iostream>
#include<unordered_map>

using namespace std;

int num_no_repeat_first(const vector<int>& ids){
    unordered_map<int, int> num_memory;
    int first_Position = -1;
    for(int i = 0; i < ids.size(); i++){
        num_memory[ids[i]]++;
    }
    for(int i = 0; i < ids.size(); i++){
        if(num_memory[ids[i]] == 1){
            first_Position = i;
            break;
        }
    }
    
    return(first_Position);


}
int main(){
    vector<int> ids = { 1,2,3,4,1 };
	auto k = num_no_repeat_first(ids);
	cout << k << endl;
	return(0);

}