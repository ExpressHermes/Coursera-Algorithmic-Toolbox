#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long int gcd(long long int a, long long int b) {
  if(!b) 
    return a;
  else
  {
    return gcd(b, a%b);
  }
  
}

long long int lcm_fast(long long int a, long long int b) {
  long long int h = gcd(a, b);
  long long int l = a * (b / h);
  return l;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_fast(a, b) << std::endl;
  return 0;
}
