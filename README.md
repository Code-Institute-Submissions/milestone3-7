

## Pablo’s Cookbook (MS3 Project)
This is Readme for my Data Centric Milestone project. 
A demo of the deployed site can be got here [Pablo's Cookbook](https://pablo-cookbook.herokuapp.com/)

<div>
    <img src="static/wireframes/Website.JPG" href="https://pablo-cookbook.herokuapp.com" target="_blank" rel="noopener" alt="website image" aria-label="website image" />
</div>
<br>





## UX

### Goals

The purpose of this website to view, add, edit and comment of recipes, the typical user is a mobile phone user who is looking for a simple clutter free website to be able to decide what recipe to choose.

### User Stories

 - As a website user I would like the ability to be able to add a recipe
 - As a website user I would like the ability to be able to edit a recipe
 - As a website user I would like the ability to be able to delete a recipe.
 - As a website user I would like the ability to search for a recipe using a key word.
 - As a website user I would like the ability to filter recipes by Course type or by Cuisine.
 - As a website user I would like the ability to view all recipes
 - As a website user I would like the ability to easily print a recipe.
 - As a website user I would like to be able to comment on a recipe
 - As a website user I would like to be able to view all comments made on a recipe.

### Wireframes


[Main page full screen](static/wireframes/Main_page_full_screen.png)

[Main page mobile screen](static/wireframes/Main_page_mobile.png)

[Recipe Page full screen](static/wireframes/Recipe_Full_Screen.png)

[Recipe Page mobile screen](static/wireframes/Recipe_Mobile.png)

[Edit recipe  full screen](static/wireframes/Recipe_edit_form_full_screen.png)

[Edit recipe mobile screen](static/wireframes/Recipe_edit_form_mobile.png)

[Add recipe  full screen](static/wireframes/Recipe_add_form_full_screen.png)

[Add recipe  mobile screen](static/wireframes/Recipe_add_form_mobile.png)



## Features

### Recipe Cards

The recipe cards were added to give the user a quick visual display of recipes. They allow a user to quickly scan through all the recipes displaying the recipe name and an image. The user can then click on the recipe mutton which will show the user the full details of the recipe. The Recipe cards are shadowed on the page to make them stand out.

### Search and Filter

The search and filter facility was put into a sidebar, this was to free up screen space on mobile devices. A button is provided in the Navbar that toggles the display of the search bar.

Users are able to filter on Course, Cuisine or Difficulty rating, there is also a free text search functionality whereby users can get all recipes that contain a specific word, this search facility also will ignore letter case of the searched word

### Recipe Add

This page allows the user to add a recipe it presents a simple form which the user must fill out. Fields are set to require so that the form must be filled out completely before it’s submitted to the database. The user has the ability to add / subtract extra ingredients or method steps. The user also has the option to cancel submitting the recipe and when click it will bring the user back to their previous page.

### Recipe edit

This page allows a user to edit recipe data that has been submitted. They can change all part of the recipe and also have the ability to add more Ingredients and method steps. When the form loads it auto populates the stored recipe data into the fields the user can then edit this data or add more data. The user has an option to cancel the request and return to the recipe page.

### Recipe Delete

This allows a user to delete a recipe, it initially displays a modal with a waring and it asks the user to confirm that they want to delete the recipe, the user also has an option to cancel the request and return to the recipe.

For the purposes of this project I have displayed the following text in the modal _“Hi this is a test website which is being graded please do not maliciously delete any recipe”_ This is because there is no user authentication requirement needed for this project, user authentication is part of the full stack project (this approach has been validated and agreed with by Code Institute)

### Recipe Comment

This allows a user to submit a comment on a recipe. Once submitted the comment will be visible in the left-hand sidebar on full screen and at the bottom of the page on a mobile.

The user also gets a confirmation message that their comment has been posted

### Recipe Print

This allows the user to click the print icon it opens the recipe in a new screen and print to the recipe to a printer.

## Database
Recipe data is stored in MongoDB

### Database collection

**recipe_data**

| Title        | Database Key          | Data Type  |
| ------------- |:-------------:| -----:|
|Recipe Id | _id | ObjectID|
| Recipe Name| recipe_name |String |
| Recipe Course| course | String|
| Recipe Cuisine|  cuisine| String|
| Recipe Image| recipe_image |String |
| Preparation Time| preparation_time|String |
| Cooking Time |   cooking_time|String |
| Difficulty Rating  |  difficulty_rating| String|
| Ingredients  |ingredients  |Array |
| Method Steps  | method_steps |Array |



**comments_data**

| Title        | Database Key          | Data Type  |
| ------------- |:-------------:| -----:|
|Comment ID | _id | ObjectID|
| Comment| comment |String |
| Recipe Id| recipe_id | ObjectID|







## Technologies Used

### Tools

PIP :  (Python Package Installer) to install packages

GIT:  Used handle version control

Github:  Used to store the code remotely

Gitpod:  Used as the IDE to develop the project

MongoDB:  Used as the database

### Libraries

Bootstrap:  To simplify the development on website and make it responsive

FontAwesome:  To provide icons used in the website

Google Fonts:  To provide styling to fonts

PyMongo:  To interface Python into Mongodb

Flask: Used to construct and render pages

## Testing

The following resources were used to test the website.

HTML -  W3 HTML Validator

CSS -   W3 CSS Validator

Google Chrome developer tools were used to test the responsiveness of the website.  Each page was tested for responsiveness across several mobile, tablet and full screen devices, all pages recited well and no issues were found. 

### Manual testing

#### Add Recipe
Click on Add Recipe in Navbar 
1.	Click submit without filling out form, error message should be display to fill out required field 
2.	Put text into Image Link section and click submit, error message should be displayed the format should be URL.
3. Fill out full recipe and clit submit, check to see that recipe is displayed in main page at bottom. 
4. Click cancel check that you return to last page you had visited. 

#### Edit Recipe. 
Pick a recipe and the select Edit. 
1. Add an extra ingredient and click Submit, check that you return to the recipe main page and that the extra ingredient was inserted, 
2. Check can you remove an ingredient or instruction 
3. Change name and then click cancel and check to see if you return to the recipe main page and the recipe is unchanged 

#### Delete Recipe. 
Pick a recipe and the select Delete. 
1. Check that a modal appears and gives you a warning. 
2. Check if you hit cancel do you return to main recipe page and the recipe is unchanged. 
3. Check if you hit delete on modal do you return to main site page. 
4. Check Mongodb database that all comments for that recipe are deleted 

#### Search Recipe. 
Using the search filter check it displays recipes correctly when filters are applied for Course, Cuisine, Dificulity Level and also Text Search 

#### Comments Testing. 
Add a comment to a recipe. 
1. Check that the comment is added and displayed in the correctly location, Right-hand side on full screed and at the bottom of the page on mobile and tablets. 
2. Check that that the message “Your comment has been recorded” is displayed at the bottom of the comments section 



## Deployment

### How to run locally

 1. Save a copy of the repository located at 		[https://github.com/pauldardis/milestone3](https://github.com/pauldardis/milestone3) by clicking the download zip button and extract the zip file to your chosen folder.
 2. if you have Git installed on your system you can clone the repository with the following command
 git clone [https://github.com/pauldardis/milestone3](https://github.com/pauldardis/milestone3)
3.	Install all required modules with the command
pip3 –r requirements.txt
4.	In your local IDE create a file called env.py. Inside the env.py file create a SECRET_KEY and a MONGO_URI to link to your own database

Example

os.environ["SECRET_KEY"] = 'your_secret'

os.environ["MONGO_URI"] = 'mongodb+srv://root:<password>@myfirstcluster-vcoqj.mongodb.net/test?retryWrites=true&w=majority'

os.environ["MONGO_DBNAME"]  ="myFirstCluster"


5.	Please make sure that you call your database cook_book and you have 2 collections called recipe_data and comments_data. You will find examples of the structure for these collections in the Database section of this Readme.
6.	You can now run the application in your IDE terminal window with the command
Python app.py

### Heroku Deployment

1. Create a requirements.txt file using the terminal command pip3 freeze > requirements.txt

2.	Create a Procfile with the terminal command 
echo web: python app.py > Procfile
3.	Git add and git commit the new Procfile and requirements.txt files to GitHub.

4.	Create a new app on Heroku website by clicking “New” give it a name and assign it to you nearest region USA or Europe.

5. From the Heroku dashboard select GitHub as the Deployment method

6. Link the Heroku app to the correct GitHub repository.

7. In the Heroku dashboard for your app click on settings “Reveal Config Vars”

8. Set the following vars

|  |  |
|--|--|
| DEBUG |FALSE  |
| IP |  0.0.0.0|
| PORT |5000  |
| SECRET_KEY | your_secret |
|MONGO_URI  |  mongodb+srv://root:<password>@myfirstcluster-vcoqj.mongodb.net/test?retryWrites=true&w=majority|

9. in the “Manual Deployment” section of the page, make sure master branch is selected and then click “Deploy Branch”

## Credits

### Content

The recipes and images used in this website have been copied from [https://www.bbc.co.uk/food/](https://www.bbc.co.uk/food/)

### Code

I have used bootstrap templates for the following parts of the website Navbar, Footer, Sidebar, Recipe Cards

### Acknowledgements

