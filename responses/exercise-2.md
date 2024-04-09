# David Lichtman

# Exercise 2

## Business Process Description - class signup

Modeling the process of signing up for a class at the Bouldering Project.  There is a signup table (fact) that applies to all signups at the gym and a class table (dim) which has details for the classes that are offered.

## Fact Table

| Column Name | Type | Description |
| --- | --- | --- |
| example | varchar | some text here |

| signup_id | int | primary key for table |
| customer_id | int | foreign key for customer dim table |
| instructor_id | int | foreign key for instructor dim table |
| timestamp | timestamp | records when transaction occurs |
| class_id | int | foreign key for class dim table |


## Dimension

| Column Name | Type | Description |
| --- | --- | --- |
| example | varchar | some text here |

| class_id | int | primary key |
| class_name | varchar | name of class |
| class_type | varchar | type of class (yoga, jiu-jitsu, climbing) |
| class_level | varchar | level of class (beginner, intermediate, advanced) |
| class_start | datetime | when class scheduled to start |
| class_end | datetime | when class is scheduled to end |
| class_price | int | price of class |
| class_location | varchar | location of class |
| max_participants | int | maximum allowed participants in class |

