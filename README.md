# COVID-19-CRAWLER-NYS

:warning: Web Crawler for the update of COVID-19 data from [New York State Government](https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases)
- The update of government official website may be behind the media/news, but it will be up-to-date by the end of the day.
- For the real-time update, I would recommend [1point3acres](https://coronavirus.1point3acres.com/?from=timeline&isappinstalled=0)
- If you are a resident at New York State, sign up for coronavirus updates [here](https://now.ny.gov/page/s/coronavirus-updates)

## Output
- Console print
- CSV file
- MongoDB

## Dependencies
```shell script
pip3 install BeautifulSoup
pip3 install PrettyTable
pip3 install lxml
pip3 install pymongo
pip3 install requests
```

## Run
- For all output
```shell script
chmod u+r+x init.sh
./init.sh
```
- For csv output
```shell script
chmod u+r+x csv.sh
./csv.sh
```

## Database
MongoDB host on [Docker](https://hub.docker.com/_/mongo)
```dockerfile
docker pull mongo
docker run -d -p 27017:27017 --name mongo_covid mongo
docker inspect mongo_covid
```
Database setup and connection
```python
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["new_york_state"]
counties = db["counties"]
```

## Result Sample - Console
```
New York State Government Official Website, Department of Health 
https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases
Last Update: March 20, 2020 | 3:25PM

+--------------------------------+----------------+
|             County             | Positive Cases |
+--------------------------------+----------------+
|             Albany             |       61       |
|            Allegany            |       2        |
|             Broome             |       2        |
|            Chenango            |       2        |
|            Clinton             |       2        |
|            Columbia            |       1        |
|            Delaware            |       1        |
|            Dutchess            |       36       |
|              Erie              |       31       |
|             Essex              |       1        |
|             Fulton             |       1        |
|            Genesee             |       1        |
|             Greene             |       2        |
|            Hamilton            |       2        |
|            Herkimer            |       2        |
|           Jefferson            |       1        |
|           Livingston           |       1        |
|             Monroe             |       32       |
|           Montgomery           |       2        |
|             Nassau             |      754       |
|            Niagara             |       3        |
|         New York City          |     4,408      |
|             Oneida             |       2        |
|            Onondaga            |       8        |
|            Ontario             |       3        |
|             Orange             |       84       |
|             Putnam             |       7        |
|           Rensselaer           |       8        |
|            Rockland            |      101       |
|            Saratoga            |       24       |
|          Schenectady           |       21       |
|           Schoharie            |       1        |
|            Suffolk             |      371       |
|            Sullivan            |       8        |
|             Tioga              |       1        |
|            Tompkins            |       7        |
|             Ulster             |       12       |
|             Warren             |       1        |
|           Washington           |       1        |
|             Wayne              |       1        |
|          Westchester           |     1,091      |
|            Wyoming             |       2        |
| Total Number of Positive Cases |     7,102      |
+--------------------------------+----------------+
2020-03-20 19:24:50,500 - Successfully crawled.
```
## Reference and Contribution
This project is based on [DXY-COVID-19-Crawler Project](https://github.com/BlankerL/DXY-COVID-19-Crawler).
All credits to [Jiabao Lin](https://github.com/BlankerL).
