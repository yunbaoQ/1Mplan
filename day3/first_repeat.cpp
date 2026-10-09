#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;




pair<int, int> firstRepeat(const vector<int>& ids) {
	int l = ids.size();
	unordered_set<int> num_count;
	int t1, t2 = -1;
	for (int i = 0; i < l; i++) {
		if (num_count.count(ids[i])) {
			t2 = i;
			break;

		}
		else {
			num_count.insert(ids[i]);
		}
	}
	for (int i = 0; i < t2; i++) {
		if (ids[i] == ids[t2]) {
			t1 = i;
			break;
		}
	}
	pair<int, int> k = { t1, t2 };
	return(k);

};
int main() {
	vector<int> ids = { 8,3,8,3 };
	auto k = firstRepeat(ids);
	cout << "{" << k.first << "," << k.second << "}" << endl;
	return(0);
};