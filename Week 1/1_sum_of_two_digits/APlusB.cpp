#include <iostream>
#define long long int ll

ll sum_of_two_digits(ll first_digit, ll second_digit) {
    return first_digit + second_digit;
}

int main() {
    ll a = 0;
    ll b = 0;
    std::cin >> a;
    std::cin >> b;
    std::cout << sum_of_two_digits(a, b);
    return 0;
}