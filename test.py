class matrix:

    def __init__(self, rows, cols, mtrx = None):
        if mtrx == None:
            self.mtrx = []
            for i in range(rows):
                self.mtrx.append(list())
            for i in range(cols):
                for e in self.mtrx:
                    e.append(0)

        else:
            self.mtrx = mtrx
        self.rows = len(self.mtrx)
        self.cols = len(self.mtrx[0])

    def __repr__(self):
        sep = ",\n"
        return f"[{sep.join(f'{e}' for e in self.mtrx)}]"
    
    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            sum = matrix(self.rows, self.cols)
            for row_index, (row1, row2) in enumerate(zip(self.mtrx, other.mtrx)):
                for entry_index, (entry1, entry2) in enumerate(zip(row1, row2)):
                    sum.mtrx[row_index][entry_index] = entry1 + entry2
            return sum
        
        else:
            raise IndexError("'matrices must have the same dimensions'")
        
    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            diff = matrix(self.rows, self.cols)
            for row_index, (row1, row2) in enumerate(zip(self.mtrx, other.mtrx)):
                for entry_index, (entry1, entry2) in enumerate(zip(row1, row2)):
                    diff.mtrx[row_index][entry_index] = entry1 - entry2
            return diff
        
        else:
            raise IndexError("'matrices must have the same dimensions'")
        
    def __mul__(self, other):
        if isinstance(self, matrix) and isinstance(other, matrix):
            product = []
            if self.rows == other.cols:
                for self_row in self.mtrx:
                    new_row = []
                    for other_row in other.transpose().mtrx:
                        new_entry = 0
                        for i in range(other.rows):
                            new_entry += self_row[i] * other_row[i]
                        new_row.append(new_entry)
                    product.append(new_row)
            return matrix(0,0, product)
        
        elif isinstance(other, int or float):
            product = []
            for row in self.mtrx:
                new_row = []
                for entry in row:
                    new_row.append(entry*other)
                product.append(new_row)
            return matrix(0,0, product)

    def __rmul__(self, other):
        return self*other
    
    def hadamard(self, *args):
        def helper_hadamard(self, other):
            had_product = (matrix(self.rows, self.cols))
            for row_index, (row1, row2) in enumerate(zip(self.mtrx, other.mtrx)):
                for entry_index, (entry1, entry2) in enumerate(zip(row1, row2)):
                    had_product.mtrx[row_index][entry_index] = entry1 * entry2
            return had_product
        
        last_had_product = (self)
        
        for m in args:
                if self.rows == m.rows and self.cols == m.cols:     
                    last_had_product = helper_hadamard(last_had_product, m)    
                else:
                    raise IndexError("'matrices must have the same dimensions'")
        return last_had_product
    
    def transpose(self):
        trans_mtrx = []

        for n in range(self.cols):
            new_row = []
            for row in self.mtrx:
                new_row.append(row[n])
            trans_mtrx.append(new_row)

        return matrix(0,0, trans_mtrx)
    
    def gauss_jordan(self):
        new_list = []

        for row in self.mtrx:
            new_row = []
            for entry in row:
                new_row.append(entry)

            new_list.append(new_row)

        reduced = matrix(0,0, new_list)

        current_row = 0

        for col_index in range(reduced.cols):
               
            hi = 0
            pivot_row = 0
            
      
            for row_index, row in enumerate(reduced.mtrx[current_row:], start=current_row):

                if abs(row[col_index]) > hi: 
                    hi = row[col_index]
                    pivot_row = row_index
            
            if hi != 0:

                reduced.mtrx[pivot_row], reduced.mtrx[current_row] = reduced.mtrx[current_row], reduced.mtrx[pivot_row]

                for entry_index in range(len(reduced.mtrx[current_row])):
                    reduced.mtrx[current_row][entry_index] /= reduced.mtrx[current_row][col_index] 

                for n in range(1,len(reduced.mtrx)-current_row):
                    for index, (entry1, entry2) in enumerate(zip(reduced.mtrx[current_row], reduced.mtrx[current_row+n])):

                        multiple = reduced.mtrx[current_row+n][col_index]
                        reduced.mtrx[current_row+n][index] -= multiple*entry1

                current_row += 1

        for row_index, row in enumerate(reversed(reduced.mtrx)):
            
            pass
                                        
            


        return reduced


        
A = matrix(0, 0, [[0, 3, 0],[0, 1, 3],[0, 0, 0]])
B = matrix(0, 0, [[1, 2, 0],[2, 2, 2],[0, 0, 0]]) 
C = matrix(0, 0, [[0, 2, 0],[0, 1, 3], [0, 3, 0]])
D = matrix(0, 0, [[0, 2, 0], [1, 3, 2]])
E = matrix(0, 0, [[3,1], [2,4], [6,7]])
F = matrix(0, 0, [[2, 4], [3, 5]])
G = matrix(0, 0, [[0, 2, 1], [3, 6, 0],[1, 4, 2]])

'''print(A+B-C)
print()
print(matrix.hadamard(A, B))
print()
print(D.transpose())
print()
print(D*E*F)

print()
print(D*3)
print()
print(3*D)
print()'''

print(G.gauss_jordan())
print()
print(D.gauss_jordan())
print()
print(E.gauss_jordan())
print()

# alex stinks