# Independent Project - Instagram-Clone

This is a Django project was generated with [Python](https://www.python.org/) version 3.9


## Author's Name
Derrick Nyongesa


## Description
This is a replica of the popular social site instagram where people share their images for other users to view. Users can sign up, login, view and post photos, search and follow other users.


## User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  


## MOCKUP DESIGN
![Mock Design](https://user-images.githubusercontent.com/78686755/119264148-974bca00-bbea-11eb-857f-9e125ccc60a6.jpg)

## Project setup instructions
1. Pull project from github Repository.

```bash
git clone https://github.com/Derrick-Nyongesa/instagram-clone.git
``` 
2. Move to the folder and create a virtual environment
3. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
4. Create a new postgress database

5. Make migrations on postgres using django
    ```bash
    $ python manage.py makemigrations <database name>
    ```
    ```bash
    $ python3 manage.py migrate
    ```
6. Run the application
    ```bash
    $ python3 manage.py runserver
    ``` 
5. Open the application on your browser `http://127.0.0.1:8000/`


## Entity relationship diagram 
![ERD - Page 1](https://user-images.githubusercontent.com/78686755/119230514-327a6c00-bb25-11eb-83df-227d3cd58ee4.jpeg)



## Technology used
* [Python3](https://www.python.org/)
* [Django3.2.2](https://docs.djangoproject.com/en/3.2/releases/3.2.2/)
* [Heroku](https://heroku.com)


## Known Bugs  
* The Image upload may not work properly, if you encounter an error, reload the page and upload again. 


##  Live Link  
 Click [View Site](https://derrick-instagram-clone.herokuapp.com/)  to visit the site

## Contact Information 
Any query? Contact me at [nyongesaderrick@gmail.com]


## Copyright and license information
Licensed under the [MIT license](LICENSE).