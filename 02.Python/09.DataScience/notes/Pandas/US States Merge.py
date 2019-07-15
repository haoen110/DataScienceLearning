import numpy as np
import pandas as pd


pop = pd.read_csv('../../data/state-population.csv')
areas = pd.read_csv('../../data/state-areas.csv')
abbrevs = pd.read_csv('../../data/state-abbrevs.csv')

pop.head()
areas.head()
abbrevs.head()

merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged.drop('abbreviation', 1)
merged.head()