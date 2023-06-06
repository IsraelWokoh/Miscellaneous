#include <iostream>
#include <string>
using namespace std;

int main() {
	float total = 0;
	int denom = 1;
	bool run = true;
	int target = 1;

	while (target <= 20) {
		cout << "Trying to reach " << target << endl;
		while (total < target) {
			try {
				float addend = 1/denom;
				total += addend;
			}
				
			catch(...) {
				cout << "Can't do any more calculations.\n";
				return 1;
			}

			
				
			denom += 1;
			cout << "\n";
		}
		cout << "Exceeded " << target << endl;
		target += 1;
	}
	
	return 0;
}