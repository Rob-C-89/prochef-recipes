## Deployment

The live deployed application can be found deployed on [Heroku](https://prochef-recipes-4b9094305975.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.

- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.

- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]

> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |

| --- | --- |

| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |

| `DATABASE_URL` | user-inserts-own-postgres-database-url |

| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |

| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)

- [Procfile](Procfile)

- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`

- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.13` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`

- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)

- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:

- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.

- *Optional*: edit your assigned cloud name to something more memorable.

- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.

- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

- `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`

- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]

> - PostgreSQL databases by Code Institute are only available to CI Students.

> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.

> - Code Institute students are allowed a maximum of 8 databases.

> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.

- An email was sent to me with my new Postgres Database.

- The Database connection string will resemble something like this:

- `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`

- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:

- `pip install whitenoise`

- Update the `requirements.txt` file with the newly installed package:

- `pip freeze --local > requirements.txt`

- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django�s "SecurityMiddleware"):

```python

# settings.py

MIDDLEWARE  = [

'django.middleware.security.SecurityMiddleware',

'whitenoise.middleware.WhiteNoiseMiddleware',

'django.contrib.sessions.middleware.SessionMiddleware',

'django.middleware.common.CommonMiddleware',

'django.middleware.csrf.CsrfViewMiddleware',

'django.contrib.auth.middleware.AuthenticationMiddleware',

'django.contrib.messages.middleware.MessageMiddleware',

'django.middleware.clickjacking.XFrameOptionsMiddleware',

'allauth.account.middleware.AccountMiddleware',

]

```

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]

> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python

import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")

os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")

os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url") # only if using Cloudinary

# local environment only (do not include these in production/deployment!)

os.environ.setdefault("DEBUG", "True")

```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`

- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `?+C` (*Mac*)

- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`

- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`

- Create a superuser: `python3 manage.py createsuperuser`

- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)

- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`

- *repeat this action for each model you wish to backup*

- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Rob-C-89/prochef-recipes).

2. Locate and click on the green "Code" button at the very top, above the commits and files.

3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.

4. Open "Git Bash" or "Terminal".

5. Change the current working directory to the location where you want the cloned directory.

6. In your IDE Terminal, type the following command to clone the repository:

- `git clone https://www.github.com/Rob-C-89/prochef-recipes.git`

7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/Rob-C-89/prochef-recipes)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Rob-C-89/prochef-recipes).

2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.

3. Once clicked, you should now have a copy of the original repository in your own GitHub account!
