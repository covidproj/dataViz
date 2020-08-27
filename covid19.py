import pandas as pd 
import io
import requests 
#New cases url
newCasesUrl="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/ecdc/new_cases.csv"
#total cases url
totalCasesUrl="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/ecdc/total_cases.csv"
#New deaths url
newDeathsUrl="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/ecdc/new_deaths.csv"
#total deaths url
totalDeathsUrl="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/ecdc/total_deaths.csv"
#recovered cases url
recoveredCasesUrl="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

newCasesContent=requests.get(newCasesUrl).content
totalCasesContent=requests.get(totalCasesUrl).content
newDeathsContent=requests.get(newDeathsUrl).content
totalDeathsContent=requests.get(totalDeathsUrl).content
recoveredCasesContent=requests.get(recoveredCasesUrl).content

newCases=pd.read_csv(io.StringIO(newCasesContent.decode('utf-8')))
totalCases=pd.read_csv(io.StringIO(totalCasesContent.decode('utf-8')))
newDeaths=pd.read_csv(io.StringIO(newDeathsContent.decode('utf-8')))
totalDeaths=pd.read_csv(io.StringIO(totalDeathsContent.decode('utf-8')))
recoveredCasesContent=pd.read_csv(io.StringIO(recoveredCasesContent.decode('utf-8')))

newCases['date']=pd.to_datetime(newCases['date'])
totalCases['date']=pd.to_datetime(totalCases['date'])
newDeaths['date']=pd.to_datetime(newDeaths['date'])
totalDeaths['date']=pd.to_datetime(totalDeaths['date'])
totalCases.columns=totalCases.columns.str.replace('World','nombre total')
newCases.columns=newCases.columns.str.replace('World','nombre de nouveaux cas')
newDeaths.columns=newDeaths.columns.str.replace('World','nombre de décès')
#pour supprimer tous les colonnes qui contiennet les noms des pays 
tableauMondeTotCas=totalCases.iloc[:,0:2]
tableauMondeNouvCas=newCases.iloc[:,0:2]
tableauMondeNouvDec=newDeaths.iloc[:,0:2]
#pour creer un tableau qui contient tous les statistiques jusqu'au aujourd'hui et qui concernent le nombre total des contaminés , le nombre de nouveaux cas de contamination et le nombre de décés pour chaque jour
tableauMonde=tableauMondeTotCas.merge(tableauMondeNouvCas[['date','nombre de nouveaux cas']])
tableauMonde=tableauMonde.merge(tableauMondeNouvDec[['date','nombre de décès']])
tableauMonde['Mois-Année']=tableauMonde['date'].dt.strftime('%b-%Y')
tableauMonde.to_csv('tabMonde.csv')
