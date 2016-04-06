class SymMatrix(object):
    def __init__(self, N, prototype=int):
        self.data = [prototype() for i in range(N*(N+1)/2)]
        
    def __getitem__(self, idx):
        x = idx[0]
        y = idx[1]
        if x > y:
            return self[y, x]
        else:
            return self.data[y*(y+1)/2 + x]

    def __setitem__(self, idx, val):
        x = idx[0]
        y = idx[1]
        if x > y:
            self[y, x] = val
        else:
            self.data[y*(y+1)/2 + x] = val