#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

int
main(void)
{
	clock_t start, end;
	vector<int> v;
	// char v[100000000];

	v.reserve(100000000);
	// v.resize(100000000);
	start = clock();
	for (int i = 0; i < 100000000; ++i)
		v.push_back(i);
		//v[i] = i;
	end = clock();
	cout << (double)(end - start) / CLOCKS_PER_SEC << endl;

	return 0;
}
