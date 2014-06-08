"""
Running regressions with Python.
"""
from scipy import stats

# set X and Y values to regress

x = [5.05, 6.75, 3.21, 2.66]
y = [1.65, 26.5, -5.93, 7.96]

# define regression output values

gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print
print "Gradient and intercept", gradient, intercept
print 
print "R-Squared", r_value**2
print
print "p-value", p_value


## Using R command types in Python
from rpy2 import rpy_classic as r

ls_fit = r.lisfit(my_x,my_y)
gradient = ls_fit['coeficients']['X']
yintercept = ls_fit['coeficients']['Intercept']

r.png('scatter_reg.png', width=400, height=350)
r.plot(x=x, y=y, xlab='x', ylab='y', xlim=(0,7), ylim=(-16,27), main="Ex Scatter Regression")
r.abline(a=yintercept, b=gradient, col='red')
r.def_off()
