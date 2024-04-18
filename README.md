# JET API Interface 

This application allows users to find nearby restaurants by postal code. 
It uses the Just Eat API to fetch restaurant data based on the postal code entered. It is oriented towards users 
form the UK and works for UK postal codes.
<br> 
It is built with Python and the Flask framework on the backend; the User Interface is built with Bootstrap and optimized for responsiveness.

[JET app demo 2.mp4](..%2F..%2FVideos%2FCaptures%2FJET%20app%20demo%202.mp4)
[JET app demo phone.mp4](..%2F..%2FVideos%2FCaptures%2FJET%20app%20demo%20phone.mp4)

## Prerequisites 
* Python 3.x
* pip 

## How to run
Running the application is pretty straightforward; you just need to clone the repository, install requirements.txt,
and you're ready to run main.py and access the application at http://127.0.0.1:5000/. More instructions below.
<details>
<summary>Option 1:Through your IDE</summary>
If you're using an IDE such as PyCharm you can clone the repository directly through their interface 
and it should take care of creating the virtual environment and installing dependencies for you. 

[pycharm-instructions.mp4](..%2F..%2FDownloads%2Fpycharm-instructions.mp4)

</details>
<details>
<summary>Option 2:Through terminal </summary>
Alternatively, you can clone and run the app in your terminal

* Clone this repository to your local machine:

```
git clone https://github.com/celinaczy/JET-api-task.git
```
* Navigate to the project directory:
```
cd JET-api-task
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
If you don't have git bash configured on your machine you can simply download and unpack a ZIP folder with this repo, 
then install dependencies by running 
```
pip install -r requirements.txt
```
run main.py and access the application on http://127.0.0.1:5000/ 
</details>

## Approach to task and assumptions
I adopted the mvp approach and started by implementing the critical requirements - making an API call within the Flask 
framework and displaying required pieces of data (Name, Cuisines, Rating - as a number, Address) on index.html. I used the 
requests package to hande the API call. As per requirements, only first 10 results are displayed. 
<br><br>
It was not requested explicitly, but I thought it only would make sense to build an interface through which the user could 
input a postal code and then be presented with the results. I used WTF Forms for this part. 
### Assumptions about Input Validation for Postal Codes
- The postal code must be between 5 and 8 characters in length.
- The input can include a space but doesn't have to.
- The input will be processed correctly regardless of whether the characters are lower or upper case.

Now, I placed this form on index.html and redirected user to restaurants.html after submitting the form with a valid postal code.
In case of the code being incorrect (returning an empty restaurant object) the user would be redirected to the home page and shown
a flash error message prompting them to input a correct code. 
<br> <br>
Once I worked out those functionalities, I moved on to improving the UI. I chose to use Bootstrap for simplicity and 
to help ensure a responsive design. I decided to display each restaurant in a separate card div and added the restaurant logo 
for a more visually pleasing effect, as I noticed the logo url was also being sent with the restaurant data. 
<br> 
I chose not to include explicit labels for the pieces of data displayed (such as: 'name:' , 'address:' ) as I found them to be 
self-explanatory. I just added a star emoji to be displayed with the rating, to ensure the user would understand what the number represents. 
<br> 
In general, I wanted to loosely replicate the way the search results are displayed on the official https://www.just-eat.co.uk/ website. 

## Improvements
I think I correctly implemented all the required functionalities, however, there are further improvements that could be made.
Some ideas for added functionalities: 
* Sort restaurants by some criteria (e.g. rating) to ensure the most relevant restaurants are being displayed 
* Allow showing more results, for example by including a 'show more' button at the bottom 
* Enhance the user interface with additional features such as filtering or sorting options

