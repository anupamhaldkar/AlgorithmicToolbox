#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    int currentrefill=0;
    int numrefill=0;
    while(currentrefill<=dist)
    {
        int r=currentrefill;
        while(currentrefill<=dist&&(stops[currentrefill+1]-stops[r])<=tank)
        {
            currentrefill+=1;
        }
        if(currentrefill==r)
        return -1;
        if(currentrefill<=dist)
        numrefill+=1;
    return numrefill;
}   }


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(n, m, stops) << "\n";

    return 0;
}
