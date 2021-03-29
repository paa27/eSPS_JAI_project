import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from cavity_relations import cavity_relations as cr


class cavity:
    def __init__(self):
        # universal properties
        sf_r_surf = 16.3605E-9
        je_r_surf = 1.3E-9
        TT = 0.7750638
        l = 0.9368514
        # ideally similar properties
        sym_cst_freq = 799.4195E6
        sym_sf_freq = 799.99E6
        sf_freq = 799.99E6
        sym_cst_omega = 2 * np.pi * sym_cst_freq
        sf_omega = 2 * np.pi * sf_freq
        sym_sf_omega = 2 * np.pi * sym_sf_freq
        sym_cst_r_over_q = 427.0822882
        sym_sf_r_over_q = 419.948
        sym_sf_G = 360.954
        # quantities dependent on normalisation

        sf_U = 49.9891826
        cst_U_ = 0.99
        sym_cst_U = 0.98
        sym_sf_U = 41.5791037
        sf_E0 = 15.73364E6
        sym_sf_E0 = 12.90208E6

        sf_Vc = TT*l*sf_E0
        sym_sf_Vc = sym_sf_E0 * TT * l
        sym_cst_Vc = 1452716.5309
        # quantities dependent on length
        sym_rf_r_shunt = 9889608.354 * l * TT
        self.TT = TT
        self.l = l
        self.sym_cst_omega = sym_cst_omega
        self.sf_omega = sf_omega
        self.sym_sf_omega = sym_sf_omega
        self.sym_cst_r_over_q = sym_cst_r_over_q
        self.sym_sf_r_over_q = sym_sf_r_over_q
        self.sym_sf_Vc = sym_sf_Vc

    def graph_U_E(self):
        sym_sf_omega = self.sym_sf_omega
        sym_cst_omega = self.sym_cst_omega
        sym_sf_r_over_q = self.sym_sf_r_over_q
        sym_cst_r_over_q = self.sym_cst_r_over_q
        sym_sf_Vc = self.sym_sf_Vc
        V_range = np.arange(0, 20E6, 1E4)
        V_range_MV = V_range/1E6
        sym_sf_U_range = cr.calc_U(V_range, sym_sf_r_over_q, sym_sf_omega)
        sym_cst_U_range = cr.calc_U(V_range, sym_cst_r_over_q, sym_cst_omega)
        sns.set_style('dark')
        g = sns.lineplot(x=V_range_MV, y=sym_sf_U_range, label='SF Model')
        sns.lineplot(x=V_range_MV, y=sym_cst_U_range, label='CST Model')
        g.axhline(cr.calc_U(8.05E6, sym_sf_r_over_q, sym_sf_omega),
                  linestyle='--', label='16GeV requirement', color='black')
        g.axhline(y=cr.calc_U(12.05E6, sym_sf_r_over_q, sym_sf_omega),
                  linestyle='--', label='18GeV requirement', color='red')
        plt.figure()
        sns.lineplot(x=V_range_MV, y=np.abs(sym_sf_U_range-sym_cst_U_range))


cav = cavity()
cav.graph_U_E()
