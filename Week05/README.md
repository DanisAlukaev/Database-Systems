## Report for the Home Assignment - Week 5.

### Populating the tables:

Tables were populated using the function `populate()` inside the file [preprocess.py](modules/service/preprocess.py). \
As in the example proposed in the lab (ref. Week 5 - Lab) this project utilizes `Faker` package for fake data creation. \
In the following screenshots depicted process of populating tables and first 17-n rows in both tables (note that in the second screenshot the number of rows is indeed 100,000). The generated data available [here](documents/customer1.csv). \
![Intermidiate step in populating](documents/Intermidiate.png) \
\
![Tables with 100,000 rows each](documents/Finished.png)

### Queries:

The created queries are aggregated in class and available in the file [queries.py](modules/service/queries.py). \
\
<b>Preliminaries.</b>\
There were created tables `customer1` and `customer2` using [database.sql](modules/service/database.sql). Then in the
mentioned above function `populate()` there iteratively executed `INSERT` queries for both tables: \
`INSERT INTO customer1(name, address, age, review) VALUES (%s, %s, %s, %s);` \
`INSERT INTO customer2(name, address, age, review) VALUES (%s, %s, %s, %s);`\
where placeholders `%s` allow inserting data using `psycopg2` package. \
\
<b>Exercise 1.</b>\
For tables `customer1` and `customer2` there were created two indexes for the attribute (column) `age` based on B-tree
and Hashing correspondingly: \
`CREATE INDEX btree_ex1 ON customer1 USING BTREE (age);` \
`CREATE INDEX hash_ex1 ON customer2 USING HASH (age);` \
In order to explore the efficiency of indexes there were executed following queries: \
`EXPLAIN ANALYZE SELECT * FROM customer1 WHERE age >= 18 AND age <= 22;` \
`EXPLAIN ANALYZE SELECT * FROM customer2 WHERE age >= 18 AND age <= 22;`\
which retrieve all customers whose age is in range of `[18, 22]` years.\
\
<b>Exercise 2.</b>\
For tables `customer1` and `customer2` there were created two indexes for the attribute (column) `review` based on GIN
and GiST correspondingly:\
`CREATE INDEX gin_ex2 ON customer1 USING GIN (to_tsvector('english', review));` \
`CREATE INDEX gist_ex2 ON customer2 USING GIST (to_tsvector('english', review));`\
In order to explore the efficiency of indexes there were executed following queries: \
`EXPLAIN ANALYZE SELECT * FROM customer1 WHERE to_tsvector('english', review) @@ to_tsquery('english', 'media | conference | camera | economic | company | cost');` \
`EXPLAIN ANALYZE SELECT * FROM customer2 WHERE to_tsvector('english', review) @@ to_tsquery('english', 'media | conference | camera | economic | company | cost');`\
which retrieve all customers whose reviews contain words "media", "conference", "camera", "economic", "company", "cost".

### Sample output:

``` 
$ python server.py

Connection has been established.
Tables 'customer1', 'customer2' were created successfully.
Populating...
Created 10000 customers.
Created 20000 customers.
Created 30000 customers.
Created 40000 customers.
Created 50000 customers.
Created 60000 customers.
Created 70000 customers.
Created 80000 customers.
Created 90000 customers.
Done!

Exercise #1: 
Before applying indexes.
Table 'customer1':  Seq Scan on customer1  (cost=0.00..4592.27 rows=7575 width=215) (actual time=0.006..14.489 rows=7500 loops=1)
Table 'customer2':  Seq Scan on customer2  (cost=0.00..4592.23 rows=7401 width=215) (actual time=0.005..14.457 rows=7500 loops=1)
Indexes for tables 'customer1' (B-tree), 'customer2' (Hash) were created successfully.
After applying indexes.
Table 'customer1':    ->  Bitmap Index Scan on btree_ex1  (cost=0.00..160.02 rows=7573 width=0) (actual time=1.062..1.062 rows=7500 loops=1)
Table 'customer2':  Seq Scan on customer2  (cost=0.00..4592.00 rows=7400 width=215) (actual time=0.006..13.572 rows=7500 loops=1)

Exercise #2: 
Before applying indexes.
Table 'customer1':  Gather  (cost=1000.00..15325.80 rows=2963 width=215) (actual time=0.615..1410.499 rows=12708 loops=1)
Table 'customer2':  Gather  (cost=1000.00..15325.80 rows=2963 width=215) (actual time=0.551..1390.802 rows=12708 loops=1)
Indexes for tables 'customer1' (GIN), 'customer2' (GiST) were created successfully.
After applying indexes.
Table 'customer1':    ->  Bitmap Index Scan on gin_ex2  (cost=0.00..145.07 rows=12409 width=0) (actual time=2.554..2.554 rows=12708 loops=1)
Table 'customer2':    ->  Bitmap Index Scan on gist_ex2  (cost=0.00..202.50 rows=2963 width=0) (actual time=23.210..23.210 rows=12708 loops=1)
```

The screenshot of output in PyCharm:
![Output](documents/Output.png)

### Conclusions.

<b>Exercise 1.</b>\
Application of B-tree index on integer attribute slightly optimizes the query in terms of cost function:  `0.00..4592.27 vs 0.00..160.02`. It does make sense, since the B-tree approach is 
suitable for data that can be sorted (ref. Week 5 - Lab). \
On the contrary, using Hash index does not influence on overall efficiency and gives compatible results before and after indexing: `0.00..4592.23 vs 0.00..4592.00`. Moreover, it is worth mentioning that
Hash index currently (PostgreSQL 13.2) does not capable of multicolumn indexing, and therefore usage of B-tree index for integer attribute `age` is more justified for future developing.  \
\
<b>Exercise 2.</b>\
Application of GIN and GiST indexes yields compatible results in terms of cost function:  `1000.00..15325.80 vs 0.00..145.07` and `1000.00..15325.80 vs 0.00..202.50`. However, in case of full text search of entries containing words "media", "conference", "camera", "economic", "company", "cost" on generated [data](documents/customer1.csv) the best performance reached with using of GIN index.