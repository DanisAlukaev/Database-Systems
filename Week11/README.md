## Report for Lab 10 - Week 11.

#### Query 1.
Find all the documents in the collection restaurants. \
\
Filter query body: `{}`. \
Query: 
```
db.restaurants.find(
  undefined
)
```
Query output: [Query 1.json](outputs/query1.json)

#### Query 2.
Find the fields restaurant_id, name, borough and cuisine for all the documents in
the collection restaurant. \
\
Filter query body: `{}`. \
Project query body: `{restaurant_id: 1, name: 1, borough: 1, cuisine: 1}`. \
Query: 
```
db.restaurants.find(
  undefined,
  {restaurant_id: 1,name: 1,borough: 1,cuisine: 1}
)
```
At export stage there were selected fields `restaurant_id`, `name`, `borough` and `cuisine`. \
Query output: [Query 2.json](outputs/query2.json)

#### Query 3.
Find the first 5 restaurant which is in the borough Bronx. \
\
Filter query body: `{borough: "Bronx"}`. Limit is set to 5. \
Query: 
```
db.restaurants.find(
  {borough: 'Bronx'}
).limit(5)
```
Query output: [Query 3.json](outputs/query3.json)

#### Query 4.
Find the restaurant Id, name, borough and cuisine for those restaurants which
prepared dish except 'American' and 'Chinese' or restaurant's name begins with
letter 'Wil’. \
\
Filter query body: `{$or: [{cuisine : {$nin : ["American ", "Chinese"]}}, {name: /^Wil/}]}`. \
Project query body: `{restaurant_id: 1, name: 1, borough: 1, cuisine: 1}`. \
Query: 
```
db.restaurants.find(
  {$or: [{ cuisine: { $nin: [ 'American ', 'Chinese' ] }},{ name: RegExp('^Wil')}]},
  {restaurant_id: 1,name: 1,borough: 1,cuisine: 1}
)
```
Query output: [Query 4.json](outputs/query4.json)

#### Query 5.
Find the restaurant name, borough, longitude and attitude and cuisine for those
restaurants which contains 'mon' as three letters somewhere in its name.  \
\
Filter query body: `{name: /.*mon.*/}`. \
Project query body: `{name: 1, borough: 1, "address.coord": 1, cuisine: 1}`. \
Query: 
```
db.restaurants.find(
  {name: RegExp('.*mon.*')},
  {name: 1,borough: 1,'address.coord': 1,cuisine: 1}
)
```
Query output: [Query 5.json](outputs/query5.json)

#### Query 6.
Find the restaurant Id, name, borough and cuisine for those restaurants which
belong to the borough Staten Island or Queens or Bronx or Brooklyn.  \
\
Filter query body: `{borough: {$in: ["Staten Island", "Queens", "Bronx", "Brooklyn"]}}`. \
Project query body: `{restaurant_id: 1, name: 1, borough: 1, cuisine: 1}`. \
Query: 
```
db.restaurants.find(
  {borough: {$in: [ 'Staten Island', 'Queens', 'Bronx', 'Brooklyn']}},
  {restaurant_id: 1,name: 1,borough: 1,cuisine: 1}
)
```
Query output: [Query 6.json](outputs/query6.json)