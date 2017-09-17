'''
Created on Sep 17, 2017

@author: DPain
'''

import numpy as np


R = np.full(shape=(11, 11),
            fill_value=-1,
            dtype=int)
NORMALIZED_Q = Q = np.zeros(shape=(11, 11),
                            dtype=int)

# The learning parameter
Gamma = 0.8


def setup_r_array():
    """
    Sets up R as a 2D array according to the example diagram.

    """
    # Hardcoded the diagram.
    for i in range(11):
        for j in range(11):
            if i == 1 and j in [2, 3, 4]:
                R[i][j] = 0
            if i == 2 and j in [5]:
                R[i][j] = 0
            if i == 3 and j in [7]:
                R[i][j] = 0
            if i == 4 and j in [1]:
                R[i][j] = 0
            if i == 5 and j in [2, 6]:
                R[i][j] = 0
            if i == 6 and j in [4]:
                R[i][j] = 0
            if i == 7 and j in [6, 8]:
                R[i][j] = 0
            if i == 8 and j in [9]:
                R[i][j] = 0
            if i == 9 and j in [8, 10]:
                R[i][j] = 0
            if i == 10 and j in []:
                R[i][j] = 0
            if i == 0 and j in []:
                R[i][j] = 0
    R[6][0] = 100
    R[7][0] = 100
    print('R Array: \n%s' % R)


def get_all_possible_actions(state):
    """
    Helper function used for the Q learning.

    Returns all the possible actions from a state.

    :param state: Current State.
    :return list of all the possible actions.

    """

    result = list()

    values = np.array(R[state])
    actions = np.where(values != -1)[0]
    for i in actions:
        result.append(Q[state][i])
    return result


def compute_q_array():
    """
    Computes the Q array based on using the Q Learning Algorithm.
    Will iterate until the Q array converges.

    """

    # Tests for convergence.
    num = 0
    while True:
        # We need to deep copies Q to old_q. Numpy quirk
        old_q = np.empty_like(Q)
        old_q[:] = Q

        num += 1
        for state in range(11):
            for action in range(11):
                possible_actions = get_all_possible_actions(action)
                if not possible_actions:
                    possible_actions = [0]
                if R[state, action] != -1:
                    Q[state, action] = R[state, action] + (Gamma * max(possible_actions))
        if np.array_equal(old_q, Q):
            print('Q Array: \n%s\nConverged with %s iterations.' % (Q, num))
            break
        elif num > 200:
            print('Q Array: \n%s\nCould not converge even with %s iterations.' % (Q, num))
            break


def normalize_q_array():
    """
    Normalizes the Q array to make it more visually representable.
    """

    highest_value = -1
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            if highest_value < Q[i][j]:
                highest_value = Q[i][j]

    for i in range(len(Q)):
        for j in range(len(Q[i])):
            NORMALIZED_Q[i][j] = Q[i][j] * 100 / highest_value
    print('Normalizd Q Array: \n%s' % NORMALIZED_Q)


def main():
    setup_r_array()
    compute_q_array()
    normalize_q_array()


if __name__ == '__main__':
    main()
