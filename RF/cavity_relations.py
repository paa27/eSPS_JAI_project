import numpy as np


class cavity_relations:
    @staticmethod
    def calc_pd_geo(Vc, r_over_q, G, r_surf=True, Q=False):
        if Q is False:
            pd = np.divide(np.square(Vc), r_over_q * np.divide(G, r_surf))
        else:
            pd = np.divide(np.square(Vc), r_over_q * Q)
        return pd

    @staticmethod
    def calc_U(Vc, r_over_q, omega):
        U = np.divide(np.square(Vc), omega * r_over_q)
        return U

    @staticmethod
    def calc_V(U, r_over_q, omega):
        V = np.sqrt(U*r_over_q*omega)
        return V

    @staticmethod
    def find_k(norm_U, norm_V):
        k = np.divide(norm_U, norm_V)
        return k
