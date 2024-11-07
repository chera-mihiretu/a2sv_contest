#include <bits/stdc++.h>
using namespace std;

int upper(vector<vector<int>> &city, int n, int number, int j){
    int start = 0, end = n - 1;
    int answer = -1;
    while (start <= end){
        int mid = start + (end - start) / 2;
        if (city[mid][j] <= number){
            start = mid + 1;
        }else{  
            end = mid - 1;

        }
    }
    return start;

}

int lower(vector<vector<int>> &city, int n, int number, int j){
    int start = 0, end = n - 1;
    int answer = -1;
    while (start <= end){
        int mid = start + (end - start) / 2;
        if (city[mid][j] < number){
            start = mid + 1;
        }else{  
            end = mid - 1;

        }
    }
    return end;
}
void solve(){
    int n, k, q;

    cin >> n >> k >> q;

    vector<vector<int>> cities(n, vector<int>{});

    for (int i =0; i < n; ++i){
        
        for (int j = 0; j < k; ++j){
            int item;
            cin >> item;
            cities[i].push_back(item);
        }
    }

    for (int i =1; i < n; ++i){
        
        for (int j = 0; j < k; ++j){
            cities[i][j] |= cities[i-1][j];
        }
    }
    

    while (q -- ){
        int m;
        cin >> m;
        vector<int> range = {1, n};
        while (m -- ){
            int j, find;
            char o;

            cin >> j >> o >> find;

            
            
            if (o == '>'){
                int index = upper(cities, n, find, j-1) + 1;
                range[0] = max(index, range[0]);
            }else{
                int index = lower(cities, n, find, j-1) + 1;
                range[1] = min(index, range[1]);
            }
        }

        // cout << range[0] << " " << range[1] << endl;
 
        if (range[0] <= range[1]){
            cout << range[0] << '\n';
        }else{
            cout << -1 << '\n';
        }

        
    }


}

int main(){

    solve();
}