sr = f['Total day calls'].sum()/f['Total day calls'].count()
f['X']= f['Total day calls'] > sr
f[f.X == True].loc[:]