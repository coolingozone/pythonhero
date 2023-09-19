import scipy.stats as stats

data_group_1 = [25, 28, 30, 32, 35]
data_group_2 = [38, 40, 45, 50, 55]

t_statistic, p_value = stats.ttest_ind(data_group_1, data_group_2)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
