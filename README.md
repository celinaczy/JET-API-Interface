# JET API Interface 

This application allows users to find nearby restaurants by postal code. 
It uses the Just Eat API to fetch restaurant data based on the postal code entered. It is oriented towards users 
from the UK and works for UK postal codes.
<br> 
It is built with Python and the Flask framework on the backend; the User Interface is built with Bootstrap and optimized for responsiveness.

## Preview
https://github.com/celinaczy/JET-api-task/assets/48793247/d86b2429-0844-41ca-a367-19ec789d3f6a

https://github.com/celinaczy/JET-api-task/assets/48793247/b3af9b4d-e394-4824-9625-4938fe9b33bf

## Prerequisites 
* Python 3.x
* pip 

## How to run
Running the application is pretty straightforward; you just need to clone the repository, install requirements.txt,
and you're ready to run main.py and access the application at http://127.0.0.1:5000/. More detailed instructions below.
<details>
<summary>Option 1: Through your IDE</summary>
If you're using an IDE such as PyCharm you can clone the repository directly through their interface 
and it should take care of creating the virtual environment and installing dependencies for you. 

https://github.com/celinaczy/JET-API-Interface/assets/48793247/88eb2ef9-a2e7-4571-92ca-dde124d30eeb

</details>
<details>
<summary>Option 2: Through terminal </summary>
Alternatively, you can clone and run the app in your terminal

* Clone this repository to your local machine:

```
git clone https://github.com/celinaczy/JET-API-Interface.git
```
* Navigate to the project directory:
```
cd JET-API-Interface
```
* Set up a virtual environment (optional but recommended):

```
# For Windows
python -m venv venv

# For macOS/Linux
python3 -m venv venv
```
* Activate the virtual environment:

```
# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate
```
* Install the required dependencies using pip:

```
pip install -r requirements.txt
```
* Run the Flask application:

```
python main.py
```
* Open your web browser and go to http://127.0.0.1:5000/ to access the application.
* When you're finished, deactivate the virtual environment:
```
deactivate
```
</details>
<details>
<summary> Option 3: Download ZIP </summary>
If you don't have Git configured on your machine or prefer not to use it, you 
can simply download and unpack a ZIP folder with this repository. Then, install dependencies by running:

```
pip install -r requirements.txt
```
run main.py and access the application on http://127.0.0.1:5000/ 
</details>

## Approach to task and assumptions
I adopted the MVP approach and started by implementing the critical requirements - making an API call within the Flask 
framework and displaying required pieces of data (Name, Cuisines, Rating - as a number, Address) on index.html. I used the 
requests package to handle the API call. As per requirements, only the first 10 results are displayed. 
<br><br>
It was not requested explicitly, but I thought it only would make sense to build an interface through which the user could 
input a postal code and then be presented with the results. I used WTF Forms for this part which meant I needed to include a
`SECRET_KEY`. I decided to hard-code it in order not to complicate the setup process and because I assumed this  application is intended 
solely for local development and there's no sensitive data involved.
### Assumptions about Input Validation for Postal Codes
- The postal code must be between 5 and 8 characters in length.
- The input can include a space but doesn't have to.
- The input will be processed correctly regardless of whether the characters are lower or upper case.

I placed this form on index.html and redirected the user to restaurants.html after submitting the form with a valid postal code.
In case of the code being incorrect (returning an empty restaurant object) the user would be redirected to the home page and shown
a flash error message prompting them to input a correct code. 
<br> <br>
Once I worked out those functionalities, I moved on to improving the UI. I chose to use Bootstrap for simplicity and 
to help ensure a responsive design. I decided to display each restaurant in a separate card div and added the restaurant logo 
for a more visually pleasing effect, as I noticed the logo URL was also being sent with the restaurant data. 
<br> <br>
I chose not to include explicit labels for the pieces of data displayed (such as: 'name:' , 'address:' ) as I found them to be 
self-explanatory. I just added a star emoji to be displayed with the rating, to ensure the user would understand what the number represents. 
<br> <br>
In general, I wanted to loosely replicate the way the search results are displayed on the official https://www.just-eat.co.uk/ website. 

## Improvements
I think I correctly implemented all the required functionalities, however, there are further improvements that could be made.
Some ideas for added functionalities: 
* Sort restaurants by some criteria (e.g. rating) to ensure the most relevant restaurants are being displayed 
* Allow showing more than 10 results, for example by including a 'show more' button at the bottom 
* Enhance the user interface with additional features such as filtering or sorting options
* Link addresses to Google Maps
