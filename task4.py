#Для проверки наличия различий между группами можно использовать однофакторный дисперсионный анализ (ANOVA).

#Нулевая гипотеза предполагает, что средние значения времени на дистанцию в трех группах равны.
# Альтернативная гипотеза предполагает, что средние значения не равны.

import scipy.stats as stats

group1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
group2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
group3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]

fvalue, pvalue = stats.f_oneway(group1, group2, group3)
print("F-value:", fvalue)
print("P-value:", pvalue)

alpha = 0.05
if pvalue > alpha:
    print("Нет достаточных оснований для ОТКЛОНЕНИЯ нулевой гипотезы")
else:
    print("ОТВЕРГАЕМ нулевую гипотезу в пользу альтернативной")

#Значение p-value равно 0.089, что больше уровня значимости 0.05.
# Это говорит о том, что нулевая гипотеза не может быть отвергнута на уровне значимости 0.05.
# Следовательно, нет статистически значимых различий между группами.