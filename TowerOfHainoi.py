def TowerOfHanoi(n,source,target,support):
    if n==1:
        print(f'disk {n} is transfered from {source} to {target}')
        return
    TowerOfHanoi(n-1,source,support,target)
    print(f'disk {n} is transfered from {source} to {target}')
    TowerOfHanoi(n-1,support,source,target)
    print(f'disk {n} is transfered from {source} to {target}')

TowerOfHanoi(3,'A','B','C')