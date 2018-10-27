# LTV

References: 

- [https://dataorigami.net/blogs/napkin-folding/18868411-lifetimes-measuring-customer-lifetime-value-in-python](https://dataorigami.net/blogs/napkin-folding/18868411-lifetimes-measuring-customer-lifetime-value-in-python)
- [https://github.com/CamDavidsonPilon/lifetimes](https://github.com/CamDavidsonPilon/lifetimes)
- [https://towardsdatascience.com/predictive-customer-analytics-part-iii-aeb996beafba](https://towardsdatascience.com/predictive-customer-analytics-part-iii-aeb996beafba)
- [https://towardsdatascience.com/whats-a-customer-worth-8daf183f8a4f](https://towardsdatascience.com/whats-a-customer-worth-8daf183f8a4f)

Kaplan Meier:  

- **LTV-Survival_Analysis from Looker**: 
 - [https://www.youtube.com/watch?v=lBijo0WhwYM](https://www.youtube.com/watch?v=lBijo0WhwYM)
 - [https://www.youtube.com/watch?v=gFc1n7Pz9zU](https://www.youtube.com/watch?v=gFc1n7Pz9zU)
- [http://savvastjortjoglou.com/nfl-survival-analysis-kaplan-meier.html](http://savvastjortjoglou.com/nfl-survival-analysis-kaplan-meier.html)
- slides: http://biostat.mc.vanderbilt.edu/wiki/pub/Main/ClinStat/km.lam.pdf

## Formulas 

Survival function: 

`S(t) = Pr(T > t)`

- T = random variable that representats subject's survival time. 
- t = a specific time of interest for T. 
- eg. S(3) = probbility of subject surviving longer than 3 time periods 

Kaplan-Meier Estimator 

` S_hat(t) = π (n_i - d_i)/ n_i ` for t_i < t 

- d_i = number of deaths at time t excluding censored data 
- n_i = number of subjects at risk of death before t 

`S_t = (# at risk at start - # that died - # censored)/ # at risk start`

## Kaplan-Meier Code 

Data needs: `duration`,`attrition_boolean`

`pip install lifelines` 

```py 
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter() 

kmf.fit(durations = df.duration, 
        event_observed = df.attrited)

kmf.event_table.head()

# survival chance of 12 months (or the given time interval unit)
kmf.predict(12)

# to plot 
kmf.plot()
# or 
# plot the KM estimate
plt.figure(figsize=(10,5))
plt.plot(kmf.survival_function_,label='KM_estimate')
plt.title("Title",fontsize='15')
plt.ylabel("ylabel",fontsize='15')
plt.xlabel("xlabel",fontsize='15')
plt.legend(fontsize='15')
plt.savefig('KM.png')
plt.show()
plt.close()        
```
