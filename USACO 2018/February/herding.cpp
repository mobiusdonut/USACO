#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    int cows [1000000] = {};
    ifstream fin;
    fin.open("herding.in");
    int n;
    fin >> n;
    cout << cows;
    cout << n;
    fin.close();
    return 0;
}
