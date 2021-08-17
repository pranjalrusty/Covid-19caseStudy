import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

#CLEANING DATA 


case_timeline=pd.read_csv(r"datasets_494724_1452107_time_series_covid_19_confirmed.csv")

cases=pd.DataFrame(case_timeline)

cases=cases.drop('Province/State',axis=1)
cases

cases_country=cases.groupby("Country/Region").sum()

cases_country=cases_country.drop(["Lat","Long"],axis=1)


cases_country.loc["India"].diff().max() #max cases in a day


max_infections = []
for cntry in cases_country.index:
    max_infections.append(cases_country.loc[cntry].diff().max())
cases_country["max_infections_rise_in_a_day"]= max_infections #column containing the maximum rise in a day for each country

cases_country["max_infections_rise_in_a_day"].max()
OUTPUT- 85687.0
# Conclusion made - The higest case rise in a day for a country is 85687.0

cases_country.index[cases_country["max_infections_rise_in_a_day"].argmax()]
OUTPUT- 'India' 
# Conclusion made - The country for the highest no of case rise is India.

cols_to_keep=['8/29/20','max_infections_rise_in_a_day']
final_cases=cases_country[cols_to_keep]
final_cases.rename(columns={'8/29/20':'Total Cases till 29/8/20'},inplace=True)
final_cases        #a final dataframe having only 'total cases' and 'maximum case rise in a day'


#HAPPINESS REPORT 


happy=pd.read_csv(r"WHR20_DataForFigure2.1.csvfinal_cases")

happy=happy[['Country name','Regional indicator','Logged GDP per capita','Freedom to make life choices']]  #keeoing only the relevant data

all=pd.merge(final_cases,happy,left_on='Country/Region',right_on='Country name')  #merging the two dataframes

all=all.set_index('Country name')



#VISUALISATIONS


cases_country.loc["India"].plot()

cases_country.loc["India"].diff().plot() #Indian stats


plt.pie(all['Total Cases till 29/8/20'],labels=all.index,labeldistance= None)
plt.title('Total Case Contributions')
plt.legend(bbox_to_anchor=(1.05, 1.0))  #country contribution pie graph



sb.regplot(all['Logged GDP per capita'],np.log(all['Total Cases till 29/8/20']))
# The above graph concludes a regression line with positive slope hence concluding that countries with higer GDP have more cases
