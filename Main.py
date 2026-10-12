import pandas as pd
import matplotlib.pyplot as plt

import analysis
import data
import visualisation

df=data.df
df=analysis.analyse_students(df)


print("After Analysis :")
print()
print(df)

visualisation.plot_student_averages(df)
visualisation.plot_subject_averages(df)
