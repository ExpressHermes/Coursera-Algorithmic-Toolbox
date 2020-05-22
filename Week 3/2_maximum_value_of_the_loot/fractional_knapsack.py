# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    ratios = []
    for w, v in zip(weights, values):
      ratios.append(v/float(w))
    
    ratios, weights, values = zip(*sorted(zip(ratios, weights, values), reverse=True))
    ratios = list(ratios)
    weights = list(weights)
    values = list(values)
    
    # print(ratios)
    for i in range(len(ratios)):
      if capacity == 0:
        break
        
      a = min(weights[i],capacity)
      value += a * ratios[i]
      capacity -= a
     
    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
