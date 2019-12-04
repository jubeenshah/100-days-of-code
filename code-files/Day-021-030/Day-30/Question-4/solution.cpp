#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int lengthOfVector, removePosition, startPosition, endPosition;
    cin >> lengthOfVector;
    vector<int> a(lengthOfVector);
    a.resize(lengthOfVector);
    for (int i = 0; i < lengthOfVector; i ++) {
        cin >> a[i];
    }

    cin >> removePosition;
    a.erase(a.begin()+removePosition-1);
    /*for (int i = 0; i < a.size(); i ++) {
        cout << a[i] << " " ;
    }*/
    cin >> startPosition;
    cin >> endPosition;
    a.erase(a.begin()+startPosition-1, a.begin()+endPosition-1);
    cout << a.size() << endl;
    //cout << startPosition << endPosition << endl;
    for (int i = 0; i < a.size(); i ++) {
        cout << a[i] << " " ;
    }
    
    return 0;
}
