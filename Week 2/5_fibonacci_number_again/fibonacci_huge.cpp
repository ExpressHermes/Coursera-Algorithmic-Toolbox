#include <iostream>
// using namespace std;

long long int get_pisano_period(long long int n) {
  int a = 0, b = 1, c = a + b;
  for(long long int i = 0; i < n * n; i++) {
    c = (a + b) % n;
    a = b;
    b = c;
    if(a == 0 & b == 1)
      return i + 1;
  }
  return -1;
}

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    // std:: cout << "Calculating pisano period...." << "\n";
    long long int pisano = get_pisano_period(m);
    n = n % pisano;
    std::cout << n << " " << pisano << '\n';
    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; i++) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    std::cout << current << '\n';
    return current % m;
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge_naive(n, m) << '\n';
}
