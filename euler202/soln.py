from sage.all import factor, prod, Subsets

def get_way_count(surface_count):
    n = (surface_count + 3) // 2
    factors = [x for x, _ in factor(n)]
    
    def f(x):
        first_k = (x * (-x % 3) - 2) // 3
        last_k = (n - 2) // 3
        last_k = last_k - (last_k - first_k) % x
        return (last_k - first_k) // x + 1

    return (n - 2) // 3 + 1 + sum( (+1 if len(subset) % 2 == 0 else -1) * f(prod(subset)) for subset in Subsets(factors) if subset)

def main():
    print(get_way_count(11))
    print(get_way_count(1000001))
    print(get_way_count(12017639147))

if __name__ == '__main__':
    main()
