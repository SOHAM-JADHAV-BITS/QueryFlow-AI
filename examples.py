
examples = [
    {
        "input":" Display the first and last names of all actors from the table actor.",
        "query":"SELECT first_name, last_name FROM actor;"
    },
    {
        "input":"Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.",
        "query":"Select upper(concat(first_name,' ',last_name)) as 'Actor Name' from actor;"
    },
    {
        "input":"Find all actors whose last name contain the letters GEN",
        "query":"select first_name, last_name from actor where last_name like '%GEN%';"
    },
    {
        "input":"Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:",
        "query":"select first_name, last_name from actor where last_name like '%LI%' order by last_name, first_name;"
    },
    {
        "input":"Add a middle_name column to the table actor. Position it between first_name and last_name.",
        "query":"alter table actor add column middle_name varchar(30) after first_name; select * from actor;"
    },
    {
        'input':"List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors",
        "query": "select last_name as 'Last Name', count(last_name) as 'Last Name Count' from actor group by last_name having count(last_name) > 1;"
    },
    {
        "input":"Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:",
        "query":"select s.first_name as 'First Name', s.last_name as 'Last Name', a.address as 'Address' from staff as s join address as a  ON a.address_id = s.address_id;"
    },
    {
        "input":"display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.",
        "query":"select concat(s.first_name,' ',s.last_name) as 'Staff Member', sum(p.amount) as 'Total Amount' from payment as p join staff as s on p.staff_id = s.staff_id where payment_date like '2005-08%' group by p.staff_id;"
    },
    {
        'input':"How many copies of the film Hunchback Impossible exist in the inventory system",
        "query":"select f.title as Film, count(i.inventory_id) as 'Inventory Count' from film as f join inventory as i on f.film_id = i.film_id where f.title = 'Hunchback Impossible' group by f.film_id;"
    },
    {
        "input":"display all actors who appear in the film Alone Trip.",
        "query":"select CONCAT(first_name,' ',last_name) as 'Actors in Alone Trip' from actor where actor_id in  (select actor_id from film_actor where film_id = (select film_id from film where title = 'Alone Trip'));"
    },

    {
        "input":" display for each store its store ID, city, and country.",
        "query":"select s.store_id as 'Store ID', c.city as 'City', cy.country as 'Country' from store as s join address as a on a.address_id = s.address_id join city as c on c.city_id = a.city_id join country as cy on cy.country_id = c.country_id order by s.store_id;"
    },
    {
        "input":"List the top five genres in gross revenue in descending order.",
        "query":"select c.name as 'Film', sum(p.amount) as 'Gross Revenue' from category as c join film_category as fc on fc.category_id = c.category_id join inventory as i on i.film_id = fc.film_id join rental as r on r.inventory_id = i.inventory_id join payment as p on p.rental_id = r.rental_id group by c.name order by sum(p.amount) desc limit 5;"
    },
    {
        "input":"Display how much business, in dollars, each store brought in.",
        "query":"SELECT s.store_id AS 'Store ID', CONCAT(c.city, ', ', cy.country) AS 'Store Location', SUM(p.amount) AS 'Total Sales' FROM payment p JOIN rental r ON r.rental_id = p.rental_id JOIN inventory i ON i.inventory_id = r.inventory_id JOIN store s ON s.store_id = i.store_id JOIN address a ON a.address_id = s.address_id JOIN city c ON c.city_id = a.city_id JOIN country cy ON cy.country_id = c.country_id GROUP BY s.store_id;"
    }
]

from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.embeddings import OpenAIEmbeddings
import streamlit as st

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(openai_api_key=),
        Chroma,
        k=3,
        input_keys=["input"],
    )
    return example_selector
