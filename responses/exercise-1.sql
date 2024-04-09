--David Lichtman
/*
Given the data sources transactions and order items,
 write and submit a SQL query that identifies
 and groups the total amount refunded by location and month.
 */

-- write your SQL here

with refunds as ( --filter to refunds only
    select * 
    from transactions
    where type='refund'
),
extract_month_from_date as ( --extract month from datetime
    select *,
    MONTH(datetime) as month
    from refunds
),
unpack_json as ( --create id and amount fields by extracting from json
    select *,
    details ->> '$.items[0].id' as id, --not sure if this is correct syntax
    details ->> '$.items[0].amount' as amount
    from extract_month_from_date
),
join_transactions_modified_with_order_items as (
    select *
    from unpack_json a
    left join order-items b ON a.id=b.id --are these the same datatype?
),
aggregate as (
    select 
    locationId as location,
    month,
    sum(amount)
    from join_transactions_modified_with_order_items
    group by 1,2
),
select * from aggregate
;
