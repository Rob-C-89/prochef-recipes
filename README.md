ReadMe

# [prochef-recipes](https://prochef-recipes-4b9094305975.herokuapp.com)

Developer: Robbie Cornell ([Rob-C-89](https://www.github.com/Rob-C-89))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Rob-C-89/prochef-recipes)](https://www.github.com/Rob-C-89/prochef-recipes/commits/main)

[![GitHub last commit](https://img.shields.io/github/last-commit/Rob-C-89/prochef-recipes)](https://www.github.com/Rob-C-89/prochef-recipes/commits/main)

[![GitHub repo size](https://img.shields.io/github/repo-size/Rob-C-89/prochef-recipes)](https://www.github.com/Rob-C-89/prochef-recipes)

[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://prochef-recipes-4b9094305975.herokuapp.com)

# Project Overview

ProChef Recipes is a website for users to view, post and comment on recipes. Designed with cooking professionals in mind, the user must create a publicly viewable profile before they can post recipes the site. Users looking to replicate the recipes can check the poster's credentials and biography, as well as read comments from the community and it's success with each recipe.

Most chefs these days will do a quick search on their phone to look for recipes, rather than checking a text book, and often whilst at work under time pressure. A lot of recipes online are from unknown and unchecked sources, or created by casual home-cooks. The concept behind ProChef Recipes is to deliver a high-standard, reliable recipe database, providing value to both professional and non-professional cooks.

I chose this subject for my personal project for Code Institute due to my background in hospitality, and my passion for a well-written, well-developed recipe by a trusted cook!

**Site Mockups**

![screenshot](documentation/mockup.png)

source: [techsini](https://techsini.com/multi-mockup/index.php)

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

- Offer website users a platform to explore and view recipe posts.

- Provide users who have created a profile to create, read, update and delete their own recipe posts.

- Let logged-in users comment on each others posts, to build an engaging community of people with shared profession and/or passion.

**Primary User Needs**

- Post-creators need easy-to-use tools for publishing and managing posts.

- Registered users need the ability to engage with recipe content through comments and account features.

- Guests need the ability to browse and enjoy recipe content without registration.

**Business Goals**

- Foster a dynamic blogging platform with active user participation.

- Build a sense of community through discussions and user engagement.

- Ensure easy recipe content management for owners, so the site's integrity can be maintained.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**

- View recipe posts as a list, with post detail available to all website visitors.

- User account features (register, log in, recipe posting, delete comments). Defensive programming to limit features to logged-in users.

- Comment and recipe post moderation and management tools for admin.

- User profile creation, with edit and delete tools.

- Recipe post management (create, read, update and delete), limited to logged-in users who have created a profile.

- Contact feature to allow users to message the owners.

- 404 error page for broken links.

#### 3. Structure

**Information Architecture**

- **Navigation Menu**:

- Links to Home, Register, Login/Logout, My Profile/Create Profile, Post Recipe

- **Hierarchy**:

- Hero image with text making the site's purpose evident to visitors.

- Recipe content displayed prominently for easy browsing.

- Clear call-to-action buttons for account creation and engagement (e.g., commenting).

**User Flow**

1. Guest users browse recipe content, view pictures, read content, and see comments.

2. Guest users register for an account, log in to leave comments, create a profile, and post a recipe.

4. Registered users leave and delete comments.

3. Registered and profiled users can create, update, and delete recipe posts.


#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**

- **[Colours](#colour-scheme)** (see below)

- **[Typography](#typography)** (see below)

### Colour Scheme

I used color-hex.com to generate my colour palette, based on the triadic colours of purple. I chose purple as my primary, darker colour for background and some text, mostly text-hover colour. Cream I used where white would be appropriate, and a slightly darker shade of teal for navbar, footer, and other elements to create a cohesive colour identity to the website.

- `#000000` primary text.

- `#660066` primary colour.

- `#fffdda` secondary colour.

- `#004C4C` accent colour.

![screenshot](documentation/color-hex-triad.png)

### Typography

- [Libre Franklin](https://fonts.google.com/specimen/Libre+Franklin) was used for the primary headers and titles, credit to Google Fonts.

- [Font Awesome](https://fontawesome.com) icons were used for the social media icons in the footer and the favicon.

## Wireframes


| Page | Desktop | Tablet |
| --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/wireframe-home.png) | ![screenshot](documentation/wireframes/mobile-wireframe-home.png) |
| Post Detail | ![screenshot](documentation/wireframes/wireframe-post-detail.png) | ![screenshot](documentation/wireframes/mobile-wireframe-post-detail.png) |
| User Profile | ![screenshot](documentation/wireframes/wirframe-profile.png) | ![screenshot](documentation/wireframes/mobile-wireframe-user-profile.png) |
| Form | ![screenshot](documentation/wireframes/wireframe-form.png) | ![screenshot](documentation/wireframes/mobile-wireframe-form.png) |



## User Stories

User stories were used for Agile development when producing this project. The project planning board can be seen [here](https://github.com/users/Rob-C-89/projects/16).

### User Story summary:

As a Site User, I can view recipes on the website and click on a recipe post to read the the full text.

As a site user, I can view comments on an each recipe post so that I can read the conversation.

As a user, I can register an account on the website so that I can access all the features of the website.

As a logged-in user, I can create a profile for the site, allowing me to showcase my bio and credentials to other users.

As a logged-in user, I can create and post my own recipes to contribute to the website content and community.

As a logged-in user, I can add and delete my own comments to contribute to the conversation around each recipe post.

As a logged-in website user, I want to be able to contact the site-owners for any number of reasons, from reporting issues, suggesting changes to the user experience, etc.

As a logged-in superuser/admin, I can delete recipe posts and users to maintain website quality.

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Recipe List | The homepage displays basic information about recipe posts, including image, title, summary and author | ![screenshot](documentation/features/home.png) |
| View Recipe Detail | Users can view the full recipe post details, including any comments. | ![screenshot](documentation/features/post-detail.png) |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Add Comments | Authenticated visitors can comment on recipe posts | ![screenshot](documentation/features/add-comment.png) |
| Delete Comments | Authenticated visitors can delete their own comments. | ![screenshot](documentation/features/delete-comment.png) |
| Create User Profile | Authenticated visitors can create a publicly viewable profile, with an image and information about themselves | ![screenshot](documentation\features\create-profile.png) |
| Edit User Profile | Registered profiled users can edit their own profile | ![screenshot](documentation\features\edit-profile.png) |
| Delete User Profile | Registered profiled users can delete their own profile | ![screenshot](documentation\features\delete-profile.png) |
| Create Recipe Post | Registered profiled users can create/publish recipe posts, including setting a featured image using Cloudinary | ![screenshot](documentation/features/post-recipe.png) |
| Edit Recipe Post | Recipe authors can edit their own posts. | ![screenshot](documentation/features/edit-recipe.png) |
| Delete Recipe Post | Recipe authors can delete their own posts. | ![screenshot](documentation/features/delete-recipe.png) |
| Contact Page | Site visitors can send a contact form to the business owners. | ![screenshot](documentation/features/contact-us.png) |
| Pagination | Recipe posts are displayed in pages, with eight posts per page. This provides better navigation for users through the post list. | ![screenshot](documentation/features/pagination.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The custom 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page. | ![screenshot](documentation/features/404.png) |

### Future Features

- **Recipe Search Functionality**: Add a search bar for users to quickly find recipes by keywords or phrases.

- **Admin Approval**: Review user profiles and recipe posts before publishing to preserve the integrity of the website.

- **Edit Comments**: Comment authors can edit their own comments, fixing typos etc. without the need to delete and re-write their comment.

- **Like/upvote Recipe Posts**: Create a points-based system, bumping popular or highly-rated recipes with more likes/upvotes up the display list or search results.

- **User messages**: Allow users to message each other through the website, to foster community and collaboration. 

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |
| [![badge](https://img.shields.io/badge/Copilot-grey?logo=githubcopilot&logoColor=##000000)](https://github.com/copilot) | Help debug, troubleshoot, and explain things. |

## Database Design

### Data Model

I have used [Mermaid](https://mermaid.ai/d/36f3bd42-c2a3-434f-815a-6cea12bc3137) to generate an interactive ERD of my project.

![screenshot](documentation\erd-mermaid.png)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/Rob-C-89/prochef-recipes/projects) served as an Agile tool for this project. Through it, User Stories were planned, then subsequently tracked on a regular basis using the Kanban project board.

### GitHub Issues

[GitHub Issues](https://www.github.com/Rob-C-89/prochef-recipes/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/Rob-C-89/prochef-recipes?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/Rob-C-89/prochef-recipes/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/Rob-C-89/prochef-recipes?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/Rob-C-89/prochef-recipes/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization
I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

At the end of project deadline, all remaining uncompleted issues were moved to Won't Have.

- **Must Have**: guaranteed to be delivered - required to publish the project

- **Should Have**: adds significant value, but not vital

- **Could Have**: has small impact if left out

- **Won't Have**: not a priority for this iteration - future features

## Testing

For all testing, please refer to the [TESTING.md](docs/TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://prochef-recipes-4b9094305975.herokuapp.com).

For detailed information on the deployment of this project, including how to clone and fork the repository, please refer to the [DEPLOYMENT.md](docs/DEPLOYMENT.md) 

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

The 'I Think Therefore I Blog' walkthrough project and module by Code Institute was used as inspiration and guidance, particularly at the beginning of the project. I expanded on this template with two custom models - UserProfile and Contact.

Much of the recipe and profile written content was generated by using Chat GPT.

Claude AI was very useful for debugging problems and explaining code logic, particularly when working evenings when tutor support was unavailable.



**Initial Research and Planning**

The following pages were very useful for inspiration and research:

Restaurant Booking PP4
https://github.com/Bear81/restaurant_booking?tab=readme-ov-file

BBC Good Food
https://www.bbcgoodfood.com/

Borough Market
https://boroughmarket.org.uk/recipes/

Great British Chefs
https://www.greatbritishchefs.com/

Django Packages
https://github.com/djangopackages/djangopackages

Django Projects
https://github.com/django/djangoproject.com

Django Social
https://github.com/djangosocialteam/djangosocial

Django projects with source code
https://www.geeksforgeeks.org/python/django-projects/

Medium guide to using MySQL
https://medium.com/@nikhilrpandey15/beginners-guide-to-django-setting-up-projects-with-mysql-03ff8cb43a44

Github community forum
https://github.com/mahmud-sajib/Community-Forum-Platform

  **Sources**

| Source | Notes |
| --- | --- |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files, ReadMe template |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Written content generation for user profiles and recipes |
| [Claude AI](https://claude.ai/) | Code logic explanation |
| [Prettier](https://prettier.io/) | Formatting code in the workspace |

### Media

All recipe and profile images on the website are my own, other than the AI generated default chef profile picture.

| Source | Notes |
| --- | --- |
| [Google Gemini](https://gemini.google.com/) | image generation for default chef image |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentors, [Tim Nelson](https://www.github.com/TravelTimN) and [Rory Patrick Sheridan](https://github.com/Ri-Dearg)  for the support throughout the development of this project.

