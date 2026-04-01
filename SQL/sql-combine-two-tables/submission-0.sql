-- Write your query below
SELECT person.first_name, person.last_name, address.city, address.state
FROM person
LEFT JOIN address
on person.person_id = address.person_id