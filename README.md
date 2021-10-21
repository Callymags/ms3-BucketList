# Bucket List
![Mock Up Image]()
* You can view the GitHub repository [here.](https://github.com/Callymags/ms3-BucketList)
* You can view the live project [here.]()

## Table of Contents
* [Project Description](#project-description)
* [UX](#ux)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)
* [Features](#features)
  * [Colour Palette](#colour-palette)
  * [Fonts](#fonts)
  * [Base Template Features](#base-template-features)
  * [Home and Landing Page Features](#home-and-landing-page-features)
  * [Register Features](#register-features)
  * [Log In Features](#log-in-features)
  * [Profile Features](#profile-features)
  * [Experience Page Features](#experience-page-features)
  * [Experience Info Features](#experience-info-page-features)
  * [Create Experience Features](#create-experience-page-features)
  * [Edit Experience Page](#edit-experience-page-features)
  * [Admin Page Log In Details](#admin-page-log-in-details)
  * [Admin Page](#admin-page-features)
  * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Libraries](#libraries)
* [Testing](#testing)
  * [User Stories](#user-stories-testing)
  * [Database CRUD Operations](#database-crud-operations-testing)
  * [User Validation](#user-validation)
  * [Responsive Design Testing](#responsive-design-testing)
  * [Browser Compatibility](#browser-compatibility)
  * [Site Performance](#site-performance)
  * [Code Validation](#code-validation)
* [Bugs Encountered](#bugs-encountered)
* [Deployment](#deployment)
  * [GitHub Pages](#github-pages)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Making a Local Clone](#making-a-local-clone)
* [Contributions](#contributions)
  * [Code](#code)
* [Acknowledgements](#acknowledgements)

## Project Description
Bucket List is a community-led website that allows users to share, create and search for bucket list ideas to put on their own customised bucket list. 

A Bucket List is a number of experiences or achievements that a person hopes to have or accomplish during their lifetime before they kick the bucket.

Users can register on the landing page and log in to the site in order to view these different ideas. They can then add these ideas to their Bucket List. Or, if they have already completed an experience, they can add it to their Done It list

This website is the third of four Milestone Projects that make up the Code Institute Full Stack Web Development Program. The main Technologies used for the site are HTML, CSS, JavaScript, Python+Flask and MongoDB


## UX: 
### Project Goals
The primary goal of this project is to create a full-stack site that users can make use of. I want users to clearly understand how the site works and create a community of users that can create, save, and search for bucket list ideas through the site.  

The secondary goal of this project is to strengthen my knowledge of Python, Flask and MongoDB. I am hoping that the challenge of developing this site will allow me to understand these three elements of the course more clearly. 

### User Stories

The main target audience can be broken into two groups: regular players and other software developers/recruiters interested in how the website was made. 

#### Regular User
As a regular user, I want: 
1. A visually appealing site no matter what device I use.
2. The ability to easily navigate through the site the first time I visit.
3. The site’s purpose to be clear once I see the landing page so I can decide if I want to register or not
4. The ability to log in and out of the site once I am registered
5. The ability to search for bucket list ideas on the site by experience name, or by experience category. 
6. The ability to view more information on a certain experience if I am interested in it. 
7. The ability to create experiences that are not already on the site, so I can share them with the community. 
8. The ability to edit an experience if I have made an error when creating it. 
9. The ability to delete an experience I have created.
10. The ability to add an experience to my own customised bucket list that I can view on my profile. 

#### Software Developer/Recruiter
As a software developer/recruiter, I want: 
1. To view the developer’s Linked In profile
2. To view the developer’s GitHub repository for the project so I can look into their code
3. The ability to examine the creator’s ReadMe for more details on how the project was created.
4. View the site and play around with its features. 


#### Developer Goals 
My personal goals for this project are as follows: 

As a developer, I want to: 
1. Develop a deeper understanding of Python, MongoDB, and Flask by creating an original project with CRUD functionality.
2. Create a professional looking project that I will be proud to put in my portfolio.

### Wireframes 
I used Balsamiq wireframes to visualise how the site would be structured on different devices. 

These wireframes were a useful reference when I began developing the basic structure for the website.

You can view the wireframes below.

* [Landing Page](static/images/wireframes/landing-page.jpg)
* [Edit Experience](static/images/wireframes/edit-experience.jpg)
* [Edit Profile](static/images/wireframes/edit-profile.jpg)
* [Experiences Info](static/images/wireframes/experience-info.jpg)
* [Home Page](static/images/wireframes/home-page.jpg)
* [Landing Page](static/images/wireframes/landing-page.jpg)
* [Profile](static/images/wireframes/profile.jpg)
* [Search Page](static/images/wireframes/search-page.jpg)

It is important to note that I did not do a wireframe for certain pages like the admin page, the log-in page, and the register page. The reason for this was a lack of adequate planning since the project deadline was due within 5 weeks of me starting the project. This meant that I rushed the initial planning of the project more than I should have and came across certain design problems as a result. 

Also, as you can see from the wireframes, there have been some changes to certain features when I began developing the pages. 

## Features 
### Colour Palette
The three main colours I chose for the website are displayed in hex format below

* Orange #ff6a3d: Used for the website brand, the font awesome icons, and the buttons on the website
* Navy #1a2238: Used for the navbar, the footer, and the badges that display the experience categories on the experience cards. 
* White #f8f8fb: Used for the font colour for buttons and nav-links on the site. I also used it for the social links in the footer. 
* Black #101112: Used for the majority of the font colours on the site. 

### Fonts
I used two different fonts for this website

* ['Crimson Text', serif:]( https://fonts.google.com/?query=crimson+text) Used for the website headings
* ['Work Sans', sans-serif:]( https://fonts.google.com/?query=work+sans) Used for all other font elements of the website. 

### Base Template Features
* Links for dependencies: All relevant CSS, bootstrap, font awesome, JavaScript/jQuery links are coded in the base template. This means that I did not need to input these dependencies into each html page. 
* Navbar: The navbar displays the website logo and all the navbar links. The user can only see certain navbar links depending on if they are logged in/out, or if they are admin/regular user. This was done through the use of flask conditional statements. 
* Footer: The footer shows the GitHub and LinkedIn social links which will open a new tab for the user to view my LinkedIn profile and my GitHub repository for this project. 
 
### Home and Landing Page Features
* Hero Image: The landing page has a hero image with a short heading within to keep the user on the site. This image covers the whole width of the page and has custom CSS styling to darken it. This allows the heading in the middle of the image to stand out more
* Latest Entries Section: This section displays the 8 most recent uploads made to the site by users. First time users can then view more information on these experiences but need to sign up/log in to add these experiences to their bucket list. 
* Experience cards: The Experience cards show an image, title, and category of an experience. The cards show the name of the user who added the experience to the site and there is a button at the end of the card to view more information on the experience. This will redirect the user to another page. 

### Register Features
* Background Image: The background image is the same one that is on the home page. 
* Register Card: The Register card looks for the user to input a username, email, and password. 
* Register Validation: If the user inputs a username/email that is already in the database, a flash message will appear just below the navbar notifying them that the username/email is already taken. 
* Username Credentials: The username must have 5-15 characters and cannot contain special characters. Otherwise, a pop-up will appear telling the user to follow this format. 
* Email Credentials: The user email must have a typical email format. Otherwise, a pop-up will appear telling the user to follow this format. 
* Password Credentials: The password must contain at least one number, one uppercase and lowercase letter, and at least 8 or more characters. Otherwise, a pop-up will appear telling the user to follow this format. 
* Redirect to Log In page: There is a link within the Register card that redirects the user to the Log In page. 
* Register Button: The user can click on the Register button once they have inputted their details. If the details are correct, they will be redirected to their new profile. 

### Log In Features
* Background Image: The background image is the same one that is on the home page. 
* Log In Card: The Log In card looks for the user’s username and password they have used when signing up to the platform. 
* Log In Validation: If the user inputs the wrong log in credentials, a flash message reading ‘Incorrect username and/or password’ will display just under the navbar informing the user of their mistake. 
* Form Validation: The user must input certain credentials into the input fields of the form or else the form will not post the data. 
* There is a specific format for the password that the user must follow. If the user inputs an incorrect format, a pop-up will notify them of the format they must follow.
* Redirect to register page: There is a link within the log in card that redirects the user to the register page. 
* Log In Button: The user can click on the log in button once they have inputted their details. If the details are correct, they will be redirected to the profile.

### Profile Features
* Welcome message: A welcome message is displayed to the user upon log in/sign up
* Profile Card: The profile card displays the user’s info. These being their username, email, and how much experiences they have created. 
* Edit Profile: The Edit Profile button redirects the user to another page with a form that allows the user to change their password. 
* Delete Profile: The user can delete their profile if they want. The delete profile button opens a modal asking the user if they are sure they want to delete their profile.  
* Bucket List Section: This section of the profile displays the user’s custom bucket list. The list if full of experiences they have saved to their profile and is styled to display the experience as cards. The user can then choose to remove these experiences from their bucket list if they want. 
* No Items in Bucket List Section: The user will see a link in the Bucket List section if they have not yet saved any items to their bucket list. The link will redirect them to the experiences page where they can browse all experiences on the site.   
* Experiences Created Section: This section of the profile displays a list of all the experiences created by the user. The experiences are shown in card format. 
* No Items in Experiences Created Section: The user will see a link in the Experiences Created section if they have not yet created any experiences on the. The link will redirect them to the Create Experience page. 
* Experience Card tooltips: The experience cards have two buttons at the bottom that will allow the user to add/remove experience from their Bucket List, or to see more information about the experience. The buttons are displayed as icons but if the user hovers over the image, there are custom styled tooltips to give the user more information as to the button’s purpose. 

### Experience Page Features
* The experience page is broken into two sections. The first section is the search and sort container, and the second section is the experience/results container 
* Search Bar: The search container features a search bar that allows the user to search the site for experiences based on the Title of the experience. 
* Reset Button: This button under the search bar will redirect the user back to the original Experiences page. 
* Sort filter: The search container also features a Sort filter that allows the user to sort all experiences by Category, or by Date Uploaded. 
* Pagination: The Sort filter returns a lot more results than a specific search query. Therefore, pagination was inputted for the filter results. The pagination only displays eight cards per page and there are links at the bottom of the experiences container to go to the next page of experiences.

### Experience Info Page Features
* The experience info shows the usual card features but also shows the experience description.
* The user can also edit/delete the experience from the Experience Info page if they are the one who created the experience. Other users will not be able to view these settings as a result of flask conditional statements inputted into the html page. 
* Delete Experience Button: The delete experience button opens a modal that asks the user if they are sure they want to delete the experience from the site. 
* Edit Experience Button: The edit experience button redirects the user to the Edit Experience Page
 

### Create Experience Page Features
* The create experience page features a form for the user to input the necessary details that give information about the experience they want to upload. 
* Experience Title Requirements: The title of the experience must be between 5 and 30 characters and the form will not post if nothing is inputted into this field. 
* Category Dropdown: The Category dropdown only allows the user to choose from a limited list of categories for their experience. Only the admin can create a new experience category. The form will not post if nothing is inputted into this field. 
* Image Address: The image address will render the image for the experience on the card. The form will not post if nothing is inputted into this field. 
* Description: The user must give the community more information about this experience by inputting more details into this field. The text area must have 5-200 characters and the form will not post if nothing is inputted into this field.

### Edit Experience Page Features
* The edit experience page is very similar to the create experience page. It features a form for the user to input the necessary details that give information about the experience they want to edit. 
* The previous experience details will be inputted by default into each of the input fields. The user can then edit the information that is displayed to them in the inputs. 

### Admin Page Log in Details
* The admin page log in details are as follows. Username: admin. Password: DVDPlayer19

### Admin Page Features
* The admin has an extra ‘Manage Categories’ link that allows the admin to add or remove an experience category. Once this category is added, a user will be able to choose this category from the dropdown menu once they are creating an experience.
* The admin also has the power to delete or edit any experience that is on the site. This is to ensure that all experience cards look clean and that there are no inappropriate cards on the site. 
* Once the admin deletes an experience, it will be deleted from all user’s bucket lists if they have saved it as it no longer exists. 

### Future Features
* Done It List: I wanted the user’s to be able to have a ‘Done It List’ on their profile also but didn’t have time to develop this feature on the site. This would have allowed users to add an experience that they have completed to their own Done It List. 
* Contact Page: The user could send a message to the developer via an email that is sent through the Contact Page
* Form.py file: Create forms.py file and all logic for form validation to be done through this file. 
* Profile Pagination: Create pagination for the bucket list and experience created section on the profile. Currently there is no pagination for these sections. 

## Technologies Used
### Languages 
* [HTML](https://en.wikipedia.org/wiki/HTML5) 
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
* [JavaScript](https://www.javascript.com/) 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 

### Frameworks
*	[jQuery:](https://jquery.com/): Used to enable tooltip functionality.
*	[Bootstrap 5.01:](https://getbootstrap.com/) Used to style the website and help with the website’s responsiveness. 
* [Google Developer Tools:](https://developer.chrome.com/docs/devtools/) Used to test responsive elements of page and to fix bugs.
* [Git:](https://git-scm.com/) Useful to control and document page versions through git commits and git pushes.
* [Github:](https://github.com/) Used to store project code and to deploy the website.
* [Mongo DB:](https://www.mongodb.com/) Used to store the data for the website
*	[Flask:](https://flask.palletsprojects.com/en/2.0.x/#) Used in site development to handle user data and python queries to database. 
* [RandomKeygen:](https://randomkeygen.com/) Used to generate a secure secret key needed in order to use certain Flask features 
* [Balsamiq:](https://balsamiq.com/) Used to draw up wireframes so I could visualise the design of the website.
* [PDF2JPG:](https://pdf2jpg.net/) Used to convert exported wireframe PDFs to JPG images that can be viewed in ReadMe. 
*	[Canva:](https://www.canva.com/) Used to create a simple logo for the website. 
* [Windows Paint 3D:](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab) Used to create a transparent PNG of the Bucket List logo created on Canva
* [Color Hunt:](https://colorhunt.co/) Used to find suitable background colours for styling.   
*	[Online-Convert.com:](https://www.online-convert.com/) Used to convert the bucket logo to favicon format to be used in the experience cards. 
* [Heroku:](https://www.heroku.com/) Used to deploy the live version of the site.


### Libraries
* [Google fonts:](https://fonts.google.com/) Used to find appropriate fonts for the website
* [Font Awesome:](https://fontawesome.com/icons?d=gallery&p=2) Provided the icons for the website buttons and the social media links in the footer. 

## Testing
### User Stories
#### Regular User
As a regular user, I want: 
1. A visually appealing site no matter what device I use.
* Bootstrap styling makes the landing page responsive and appealing at all screen sizes. 
2. The ability to easily navigate through the site the first time I visit.
* Conventional structure of the site ensures that the user will intuitively know how to navigate through the page.
3. The site’s purpose to be clear once I see the landing page so I can decide if I want to register or not
* The landing page does give a general sense of what the website is about. However, it does need more information on the user features and the benefits of becoming a user.  
4. The ability to log in and out of the site once I am registered
* Users can log in/out with ease
5. The ability to search for bucket list ideas on the site by experience name, or by experience category. 
* Users can search for an experience by its title, or they can sort all experience by date uploaded and category.
6. The ability to view more information on a certain experience if I am interested in it. 
* Information button on experience card will direct user to page with more information on experience
7. The ability to create experiences that are not already on the site, so I can share them with the community. 
* A logged in user can create an experience by selecting the Create Experience link in the navbar. 
8. The ability to edit an experience if I have made an error when creating it. 
* A user can edit an experience if they were the ones that created it. 
9. The ability to delete an experience I have created.
* User can delete experience if they were the person who created it. 
10. The ability to add an experience to my own customised bucket list that I can view on my profile. 
* Bucket list section on profile that is customised for each individual user. 

#### Software Developer/Recruiter
As a software developer/recruiter, I want: 
1. To view the developer’s Linked In profile
* Link to my LinkedIn profile in the website footer
2. To view the developer’s GitHub repository for the project so I can look into their code
* Link to the project’s GitHub repository in the footer of the website 
3. The ability to examine the creator’s ReadMe for more details on how the project was created.
* ReadMe features a detailed description of the project’s purpose, how the project was made, the projects testing, and the project’s deployment details
4. View the site and play around with its features. 
* Live site deployed to Heroku. Link at the top of ReadMe. 

### Database CRUD Operations Testing:
#### Read Operations:
* Landing Page and Home Page: The last eight experiences entries into the database are shown to the user
* Experiences Page: A card is loaded for every movie in the database on the experiences page.
* Experiences Page: Results are sorted into specific groups based on the Sort filter.  
* Search Page: Experiences are pulled from the database if they match the search options for the experience title.
* Experience Card: If clicked on, the experience card redirects to a page that gives more information on that specific experience. 
* Profile: User profile cards gives the user details on their username and email that are saved to the database. 
* Admin: A card is loaded for every category in the database. This can be seen in the Manage Categories section that can only be seen by the admin.  

#### Create Operations:
* Sign Up: When a user signs up, a new user is created in the user collection with details on their username, email, password. An empty array is also created for the user’s Bucket List so they can add experiences to this array
* Create Experience: When a user adds a new experience, it enters the experience collection with relevant fields. The experience’s ID is also added to the user's Created Experiences list.
* Add Category: The site admin can add more categories to the categories collection in the database by selecting the add category option through the site. This new category can then be selected by other users when they are creating experiences. 

#### Update Operations:
* Experiences: A user can edit an experience they have created by filling out an edit experience form. This experience will then be updated in the database.
* Admin: The site admin can edit all experiences on the website. These changes will the be updated in the database. 
* Edit Profile: Any user can change their password by updating inputting a new password into the new password input field on the Edit Profile page. This old password will then be updated in the database.  

#### Delete Operations:
* Experiences: When the user/admin deletes an experience, it is removed from the database and their Bucket List.
* Delete Profile: A user can delete their profile from the database by selecting the Delete Profile button in their profile. 
* Remove from Bucket List: A user can remove an experience from their Bucket List, and this will delete the experience from the Bucket List array in the database. 

### User Validation:
#### Login Validation:
* Users can't login with an incorrect password. 
* Users can't login with the incorrect username.

#### Sign Up Validation:
* Users can't create an account with a username that is already in the database. 
* Users can't create an account with an email that is already in the database. 

### Responsive Design Testing
The website layout was tested on the following physical devices: 
* Huawei P20 Lite (Google Chrome)
* iPad (Safari)
* Fujitsu Lifebook A512 (Google Chrome)
* Hp L1906 (Google Chrome)

Google Chrome Developer Tools was also used to test the responsiveness of the site using the following devices. 
* Moto G4 
* Galaxy S5
* Pixel 2 
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold
* Nest Hub
* Nest Hub Max

### Browser Compatibility
Browser compatibility was physically tested across the different browsers listed below: 
* Google Chrome Version 89.0.43389.114
* Microsoft Edge Version 89.0.774.68
* Mozilla Firefox Version 87.0
No problems were found