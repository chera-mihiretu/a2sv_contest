#include <bits/stdc++.h>
#define int uint64_t
#define SPEEDY std::ios_base::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0);
int rangeXOR(int left, int right){
    if (left == 0){
        if (right % 4 == 0)
            return right;
        if (right% 4 == 1)
            return 1;
        if (right% 4 == 2)
            return right + 1;
        
        return 0;
    }else{
        return rangeXOR(0, left - 1) ^ rangeXOR(0, right);
    }
}


void solve(){

    // accepting the values

    int left, right, i, k;

    std::cin >> left >> right >> i >> k;

    int allXOR = rangeXOR(left, right);
    
    int left_bound;
    int right_bound;

    left_bound = left >> i;
    right_bound = right >> i;

    if (((left_bound << i) | k) < left){
        left_bound ++ ;
    }

    if (((right_bound << i) | k) > right){
        right_bound -- ;
    }

    int non_beauty = rangeXOR(left_bound, right_bound);


    if ((right_bound - left_bound) % 2 == 0){
        non_beauty  = (non_beauty << i) | k;
    }else{
        non_beauty = non_beauty << i;
    }

    

    int answer = non_beauty ^ allXOR;

    std::cout << answer << "\n";

}



int32_t main (){
    
    int test;
    std::cin >> test;
    while (test -- ){
        solve();
    }

}