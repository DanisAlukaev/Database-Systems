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
Table 'customer1':  Seq Scan on customer1  (cost=0.00..4589.85 rows=7578 width=215) (actual time=0.006..14.030 rows=7531 loops=1)
Table 'customer2':  Seq Scan on customer2  (cost=0.00..4589.80 rows=7394 width=215) (actual time=0.005..14.078 rows=7531 loops=1)
Indexes for tables 'customer1' (B-tree), 'customer2' (Hash) were created successfully.
After applying indexes.
Table 'customer1':  Bitmap Heap Scan on customer1  (cost=161.92..3364.51 rows=7573 width=215) (actual time=1.315..4.014 rows=7531 loops=1)
Table 'customer2':  Seq Scan on customer2  (cost=0.00..4589.00 rows=7390 width=215) (actual time=0.007..13.104 rows=7531 loops=1)

Exercise #2: 
Before applying indexes.
Table 'customer1':  Gather  (cost=1000.00..15322.80 rows=2963 width=215) (actual time=0.741..1376.895 rows=12533 loops=1)
Table 'customer2':  Gather  (cost=1000.00..15322.80 rows=2963 width=215) (actual time=0.717..1377.796 rows=12533 loops=1)
Indexes for tables 'customer1' (GIN), 'customer2' (GiST) were created successfully.
After applying indexes.
Table 'customer1':  Bitmap Heap Scan on customer1  (cost=74.96..4025.99 rows=2963 width=215) (actual time=2.856..6.206 rows=12533 loops=1)
Table 'customer2':  Bitmap Heap Scan on customer2  (cost=203.24..4154.27 rows=2963 width=215) (actual time=23.234..566.453 rows=12533 loops=1)
```