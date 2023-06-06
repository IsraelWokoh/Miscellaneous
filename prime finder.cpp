#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <iterator>
#include <set>
using namespace std;

int dgtlRoot(int number) {
	int root = 0;
	for (auto digit: to_string(number)) {
		// int integer = digit;
		// total += integer;
		// int integer = std::atoi(digit);
		// cout << typeid(digit).name() << endl;
		// cout << digit << endl;
		root += (int)digit-48; // (int)digit changes to ASCII value
		// subtract 48 to get actual value
	}

	if (root >= 10) {
		return dgtlRoot(root);
	} else {
		return root;
	}
	// if (total >= 10) {
	// 	return dgtlRoot(total);
	// }
}

bool isPrime(int num) {
	set<double, greater<double> > factors; // Stores factors of num
	for (int divisor = 0; divisor <= sqrt(num); divisor++) {
		if ("245680".contains(to_string(num%10)) && {2,5}.contains(num)
		|| !(dgtlRoot(num) % 3) && num == 3) {
			return true;
		}
		
	}
	return true;
}

int main() {
	int myInt = 1396412423;
	cout << "Digital root of " <<
	myInt << ": " << dgtlRoot(myInt)
	<< endl;
	return 0;
}