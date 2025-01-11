#include <bits/stdc++.h>

using namespace std;
int arr[200200];
int n, h;
int solve(int index, int health, int green, int blue){


    if (index == n) return 0;
    if (health < arr[index]) return solve(index + 1, health +( arr[index] / 2), green, blue) + 1;
   
    int g_ans = (green ? solve(index, health * 2, green - 1, blue) : 0);
    int b_ans = (blue ? solve(index, health * 3, green, blue - 1) : 0);
    return max(g_ans, b_ans);
    
}

int main(){
    int test;
    cin >> test;
    while (test) {
        
        cin >> n >> h;
        
        for (int i =0; i < n; ++i) cin >> arr[i];
        sort(arr, arr + n);
        cout << solve(0, h, 2, 1) << endl;
        test--;
    }
}