-- B-Tree section

-- Query 1.

-- Before applying:
--      Hash Join  (cost=510.99..12062691.37 rows=14596 width=70) (actual time=22.557..64342.399 rows=14596 loops=1)
DROP INDEX amount_payment_index;

-- After applying:
--      Hash Join  (cost=510.99..11659130.21 rows=14596 width=70) (actual time=16.934..40902.928 rows=14596 loops=1)
CREATE INDEX amount_payment_index ON payment (amount);

-- TRIED:   CREATE INDEX rental_id_payment_index ON payment (rental_id);
--          DROP INDEX rental_id_payment_index;
--
--          CREATE INDEX rental_id_rental_index ON rental (rental_id);
--          DROP INDEX rental_id_rental_index;

EXPLAIN ANALYZE select *, (select count(*) from rental r2, payment p2 where
r2.rental_id = p2.rental_id and p2.amount<p.amount) as
count_smaller_pay from rental r, payment p where r.rental_id =
p.rental_id;

-- Query 2.

-- Before applying:
--      Nested Loop Anti Join  (cost=534.78..2284549.49 rows=9731 width=10) (actual time=8767.066..26962.442 rows=1 loops=1)
DROP INDEX last_updated_rental_index;

-- After applying:
--      Nested Loop Anti Join  (cost=535.06..1557083.92 rows=9731 width=10) (actual time=21.287..50.309 rows=1 loops=1)
CREATE INDEX last_updated_rental_index ON rental(last_update);

-- TRIED:   CREATE INDEX last_updated_customer_index ON customer(active);
--          DROP INDEX active_customer_index;
--
--          CREATE INDEX customer_id_payment_index ON customer (customer_id);
--          DROP INDEX customer_id_payment_index;
--
--          CREATE INDEX customer_id_rental_index ON rental (customer_id);
--          DROP INDEX customer_id_rental_index;

EXPLAIN ANALYZE
SELECT r1.staff_id, p1.payment_date
FROM rental r1, payment p1
WHERE r1.rental_id = p1.rental_id AND
NOT EXISTS (SELECT 1 FROM rental r2, customer c WHERE r2.customer_id =
c.customer_id and active = 1 and r2.last_update > r1.last_update);

-- Query 3.

-- Before applying:
--      HashAggregate  (cost=7747.19..7747.20 rows=1 width=40) (actual time=134.656..134.658 rows=1 loops=1)
DROP INDEX rental_duration_film_index;
DROP INDEX phone_address_index;

-- After applying:
--      HashAggregate  (cost=5364.11..5364.12 rows=1 width=40) (actual time=131.197..131.199 rows=1 loops=1)
CREATE INDEX rental_duration_film_index ON film(rental_duration);
CREATE INDEX phone_address_index ON address(phone);

-- TRIED:   CREATE INDEX rating_film_index ON film(rating);
--          DROP INDEX rating_film_index;
--
--          CREATE INDEX length_film_index ON film(length);
--          DROP INDEX length_film_index;
--

EXPLAIN ANALYZE
select f1.release_year, max(f2.rating), (select max(phone) from
address) as max_phone from film f1, film f2 where f1.length > 120 and
f1.rental_duration>f2.rental_duration group by f1.release_year;
