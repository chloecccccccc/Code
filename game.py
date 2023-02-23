# coding: utf-8 -*-
# description: play game
import random


class Point(object):
    def __init__(self, idx):
        self.idx = idx
        self.point_name = 'point_' + str(idx)
        self.next_points = []
        self.prev_points = []

    def add_point(self, next_points, prev_points):
        self.next_points = next_points
        self.prev_points = prev_points


point_1 = Point(1)
point_2 = Point(2)
point_3 = Point(3)
point_4 = Point(4)

point_1.add_point([point_2, point_3], [point_3])
point_2.add_point([point_3], [point_1])
point_3.add_point([point_1, point_4], [point_1, point_2])
point_4.add_point([], [point_3])

points = [point_1, point_2, point_3, point_4]

start_point = random.choice(points[:3])
print("starting point: " + start_point.point_name)

infinite_times = 100
loop_idx = [[1, 3], [3, 1]]
ae_idx = []
loop_count = 0
while True:
    A = random.choice(start_point.next_points)
    print("A from point " + start_point.point_name + ' to ' + A.point_name)
    ae_idx.append(A.idx)
    if A.idx == point_4.idx:
        print('A wins!' + '\n')
        break

    else:
        avail_idx = []
        for point in A.next_points:
            avail_idx.append(point.idx)
        E_idx = int(input('The current vertex is:' + str(A.idx) + ', Please enter the next vertex where E moves to, the available vertices are:' + str(avail_idx)) + '\n')
        while E_idx not in avail_idx:
            E_idx = int(input('Input error, please re-enter the next vertex that E moves to, the available vertices are:' + str(avail_idx)) + '\n')
        E = eval('point_' + str(E_idx))
        print("E from point: " + A.point_name + 'to: ' + E.point_name)
        ae_idx.append(E.idx)
        start_point = E
        if E.idx == point_4.idx:
            print('E wins!')
            break
        if ae_idx in loop_idx:
            loop_count += 1
            if loop_count == infinite_times:
                print("A and E stay in two-cycle {1, 3}, E wins!")
                break
        else:
            loop_count = 0
        ae_idx = []

