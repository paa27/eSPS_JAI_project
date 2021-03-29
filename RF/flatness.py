import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class flatness:
    def __init__(self):
        def read_ascii_to_pd(filepath):
            data = pd.read_table(filepath)
            return data
        self.read_ascii_to_pd = read_ascii_to_pd

    def plot_flatness(self, filepath):
        data = self.read_ascii_to_pd(filepath)
        data.columns = ['x', 'E(x)', 'nothing']
        for i in data['x'].index:
            if data['x'][i] < 10:
                data.loc[i] = np.nan
        print(data)
        cor = sns.lineplot(data=data, x=data['x'], y=np.abs(
            data['E(x)']), color='black', label='On axis E-field magnitude')
        cor.set_xlabel('x [cm]')
        cor.set_ylabel('E [arbitrary units]')
        cor.axhline(np.max(data['E(x)']), ls='--', color='red')
        cor.axhline(np.max(np.abs(data['E(x)'])[:700]), ls='--', color='red')


plotter = flatness()
plotter.plot_flatness('e_field.TXT')
