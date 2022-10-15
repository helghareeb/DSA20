# بسم الله الرحمن الرحيم

## Rules

### Any live cell with fewer than two live neighbours dies (underpopulation)
### Any live cell with two or three live neighbors lives on to the next generation
### Any live cell with more than three live neighbours dies, as if by overpopulation
### Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

import matplotlib.pyplot as plt

class Life:
    def __init__(self, initial=None):
        if initial:
            self._initial = initial
        else:
            # 5 x 5 Initial Matrix
            # Surrounded by Border with Zero Values
            self._initial = [
                [0,0,0,0,0,0,0],
                [0,1,1,0,1,1,0],
                [0,1,0,1,0,1,0],
                [0,0,1,1,1,0,0],
                [0,1,1,0,1,1,0],
                [0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0]
            ]
        self._rows = len(self._initial)
        self._cols = len(self._initial[0])
        self._next = []
        self.flag = False

    def check_underpopulation(self, mat, r,c, res):
        # if mat[r-1][c-1] + mat[r-1][c] + mat[r-1][c+1] + mat[r][c-1] + mat[r][c+1] + mat[r+1][c-1] + mat[r+1][c] + mat[r+1][c+1] < 2:
        #     res[r][c] = 0
        if self.find_sum_around_me(mat, r, c) < 2:
            res[r][c] = 0

    def check_overpopulation(self, mat, r, c, res):
        # if mat[r-1][c-1] + mat[r-1][c] + mat[r-1][c+1] + mat[r][c-1] + mat[r][c+1] + mat[r+1][c-1] + mat[r+1][c] + mat[r+1][c+1] > 3:
        #     res[r][c] = 0
        if self.find_sum_around_me(mat, r, c) > 3:
            res[r][c] = 0

    def check_reproduction(self, mat, r, c, res):
        # if mat[r-1][c-1] + mat[r-1][c] + mat[r-1][c+1] + mat[r][c-1] + mat[r][c+1] + mat[r+1][c-1] + mat[r+1][c] + mat[r+1][c+1] == 3:
        #     res[r][c] = 1
        if self.find_sum_around_me(mat, r, c) == 3:
            res[r][c] = 1

    def next_generation(self):
        if self.flag:
            self._initial = self._next[:]
            for r in range(self._rows):
                for c in range(self._cols):
                    self.check_underpopulation(self._next,r,c,self._initial)
                    self.check_overpopulation(self._next,r,c,self._initial)
                    self.check_reproduction(self._next,r,c,self._initial)
            # self.plot_generation(self._initial)
            return self._initial
        else:
            self._next = self._initial[:]
            for r in range(self._rows):
                for c in range(self._cols):
                    self.check_underpopulation(self._initial,r,c,self._next)
                    self.check_overpopulation(self._initial,r,c,self._next)
                    self.check_reproduction(self._initial,r,c,self._next)
            # self.plot_generation(self._next)
            return self._next
    
    def get_mat_item(self, mat, r, c):
        if mat[r][c]:
            return mat[r][c]
        else:
            return 0

    def find_sum_around_me(self, mat, r, c):
        sum = 0
        try:
            sum += self.get_mat_item(mat,r-1, c-1)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r-1, c)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r-1, c+1)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r, c-1)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r, c+1)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r+1, c-1)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r+1, c)
        except:
            sum += 0
        try:
            sum += self.get_mat_item(mat,r+1, c+1)
        except:
            sum += 0
        return sum

    def plot_generation(self, mat):
        mat_data = []
        for i in range(len(mat)):
            mat_data.append(mat[i])
        mat_dataset = tuple(mat_data)
        plt.matshow(mat_dataset)
        plt.show()

def main():
    pass
    # life = Life()
    
    # from matplotlib.animation import FuncAnimation
    # n_frames = 3
    # fig = plt.figure()
    # plot = plt.matshow(life._initial, fignum=0)

    # def init():
    #     plot.set_data(life._initial)
    #     return [plot]

    # def update():
    #     plot.set_data(life.next_generation())
    #     return [plot]

    # anim = FuncAnimation(fig, update, init_func=init, frames=n_frames, interval=30, blit=True)
    # plt.show()
    # # life.plot_generation(life._initial)
    # # life.next_generation()




if __name__ == '__main__':
    main()