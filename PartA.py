Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

total_combinations=len(Die_A)*len(Die_B)
print("Total Combinations:",total_combinations)
matrix=[[0]*len(Die_A) for _ in range(len(Die_B))]
# Logic: The matrix is generally the sum of i+1 and j+1 indexes
# matrix = [[(i+1) + (j+1) for j in range(columns)] for i in range(rows)]
#Total combinations
s=[[(i, j) for i in Die_A] for j in Die_B]
print("-----------------------------------------------------------")
print("Possible Combinations:")
for row in s:
    print(row)
h={}
for i in range(len(Die_A)):
    for j in range(len(Die_B)):
        sum=Die_A[i]+Die_B[j]
        matrix[i][j]=sum
        if sum in h:
            h[sum]+=1
        else:
            h[sum]=1
            
print("-----------------------------------------------------------")
print("The Distribution of Possible Combinations:")
for row in matrix:
    print(row)



print("-----------------------------------------------------------")
print("Probability of all Possible Sums:")
for k, v in h.items():
    probability=v/total_combinations
    print(f"Sum: {k} - Probability: {v}/{total_combinations}")


