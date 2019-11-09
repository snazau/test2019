#include <iostream>

using namespace std;

const int NMAX = 1e2 + 5;

int dp[NMAX][NMAX];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;

    for (int digit = 0; digit <= 9; ++digit) {
        dp[1][digit] = 1;
    }

    for (int num_len = 2; num_len <= n / 2; ++num_len) {
        for (int sum = 0; sum <= num_len * 9; ++sum) {
            for (int i = 0; i <= 9 && sum - i >= 0; ++i) {
                dp[num_len][sum] += dp[num_len - 1][sum - i];
            }
        }
    }

    int answer = 0;
    for (int sum = 0; sum <= (n / 2) * 9; ++sum) {
        // for every number with sum of left (n / 2) digits that equals to sum
        // exists dp[n / 2][sum] numbers with sum of right (n / 2) digits that equals to sum
        answer += (dp[n / 2][sum] * dp[n / 2][sum]);
    }
    cout << answer;


    return 0;
}
