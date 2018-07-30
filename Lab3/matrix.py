# takes the number of rows and columns and makes a matrix of those dimensions

def make_matrix(r, c):
    matrix=[0]*r
    for i in range(r):
        matrix[i]=[0]*c
    return matrix


# takes two matrices and multiplies them returning the resulting matrix
def matrixmult(a,b):
    if len(a[0])==len(b):
        product=make_matrix(len(a),len(b[0]))
        for i in range(len(product)):
            for j in range(len(product[0])):
                temp=0
                for n in range(len(b)):
                    result[i][j]+=float(a[i][n])*float(b[n][j])
        return result
    else:
        return []



# prints the given matrix, mostly for testing purposes
def print_matrix(m):
    print(matrixmult(a,b))


# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.
def markov_simulation(ini_matrix, tans_matrix, sim_num):
    val = 0
    for i in range(sim_num):
        loop = True
        moves = 0
        temp_matrix = matrixmult(ini_matrix, tans_matrix)
        while loop == True:
                temp_matrix = matrixmult(temp_matrix, tans_matrix)
                moves += 1

                if float(temp_matrix[0][11]) > float(0.99):
                    val += moves
                    loop = False

    return float(val)/sim_num

if __name__ == '__main__':
    markov_simulation()

