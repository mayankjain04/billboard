# Billboard

*[Billboard](https://billboard.pythonanywhere.com) is a forum website created by @mayankjain04 using flask. It has a simple and user-friendly interface while maintaining some useful and advanced features.*

## Video Demo: 

## Description:
   This Project is built using flask, so the `app.py` file handles the backend and routing. `templates` folder contains the html files and their css is stored in `static` folder. `helpers.py` has some helper functions that are imported in `app.py`. `templates/layout.html` is the layout file that is extended by other html files through jinja2. 

   The idea for billboard came from the popular forum site 4chan. While 4chan has a large community and an endless amount of messages being posted everyday, we wanted to build something that improves on that. We took further inspiration from platforms like reddit and Tumblr and finally decided to build a site that doesnt require an account or verification. 
   Billboard has a unique design and a tempting layout, and while the site keeps changing little by little day after day, we aspire to improve it all the more for the sake of an environment we can all participate and enjoy in. 



## Features
   * Bllboard started out as a single page forum where you could use any username and post messages, accounts were not necessary, so at the time of launch, anyone could use any username. This was the early access version and through trial and error, we have come a long way.
   * Update 1.1
       This update came with the highly anticipated(lol) login feature, with password protection now users could secure a username for themselves to use in future to keep the their identiy hidden while still emanating a virtual presence. Along with this came the profile page, which only contains the posts of the user, but, an unexpected feature this update had, was the name change feature. I was skeptical at first, but later decided on adding this one as well, along with the change password feature.
   * Update 1.2
      This update was the biggest one yet, and took the most time and effort. It included the light and dark themes. This, along with beautiful backgroung images, made billboard more enticing and overall enhanced the user experience. Now the website expanded by having multiple pages like support, feedback, report along with the previously added register, login, and profile page. This update made the website more fun and interactive by leveraging javascript capabilities, jquery and localstorage.

Currently these features are implemented:

   ### Early access
      * Easy to use navigation features
      * An anonymous forum for posting text messages.
   ### Update 1.1
      * register and login pages
      * unique usernames
      * Profile pages, profile viewing
      * Update username/password
   ### Update 1.2
      * Themes - Light, Dark
      * major layout enhancements
      * Report posts and feedback/support for removal
      * increased interactiveness

This features are currently being developed:
* Like/dislike counts:
   We are planning to include the like dislike cound on each post. Along with this, the profile of the user will contain the total number of accumulated likes.
* Share and Mention:
   The messages can be replied to and mentioned. furthermore, usernames can be tagged in a message.
* Online users:
   The web will show the total number of active users at any time. 
* Data saving mode:
   The backgound images can be turned off, and some other background processes can be optimized when user enables the data saving mode.

Billboard keeps improving thanks to all the feedback and reccomendation received from the users, and many of the planned out features are requested by the users as well. Currenly these features have been planned to be integrated in the future.
* Theme customization:
   The user can choose colors and gradiants to apply to the site, making it custom to their taste.
* Monochrome mode/theme:
   A new theme, that gives users a minimalistic experience.
* Posting images:
   Posting images along with their texts.
* Special username privileges like flair and highlights:
   More active users will have special flairs, while everyone can choose their flair from their profile.
* Censoring certain words and phrases:
   A feature when enabled, censors vulger and offensive words.
* Account deletion:
   Parmanently deleting your account along with posted texts and images.

These features will be released as soon as they are developed and will be considered a part of the next major update. 

## Quickstart
While the website thus far has been solely designed and managed be me alone, you are more than welcome to fork this directory and make modifications. I am currently planning to keep this work open source so contributions from users bring us motivation to strive for more.
You may work on it in your preferable IDE, or clone it directly in a pythonanywhere accont to start testing and deployment.

The below method is for deploying the site from your own pythonanywhere account:
The `main` branch can be cloned directly in your pythonanywhere directory. Patch-1 contains newer features not yet applied on webpage.
* Clone `patch-1`
* Set up a venv with dependencies and requirements.
* Set up a MySQL database
   * Configure host in `app.py`
   * Execute queries present in `queries.sql`

## Website
The website has been made live thanks to pythonanywhere by anaconda.
* [Billboard](https://billboard.pythonanywhere.com)
* [Code](https://github.com/mayankjain04/billboard)

## Connect
*Founder: Mayank Jain*

   I am an IT engineering student, learning web devolopment and other stuff. Billboard was created as a final project to my cs50x course, but working on it made me realise its potential as a social media platform.
   * [LinkedIn](https://www.linkedin.com/in/mayank-jain-395bb3295?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

 