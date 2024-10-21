**Project Documentation - Overview and Setup Guide**
====================================================

**Project Overview**
--------------------

This project is a travel-based web application that displays **featured places** and **galleries** of popular destinations around the world. The app dynamically loads featured places and gallery items, which are stored in a JSON file, allowing easy management and updates of the content. The app is built using **Django** for the backend, with templated HTML for the frontend, styled using static assets (CSS, JavaScript, and images).

### **Key Features**

-   **Home Page**: Displays a list of featured places around the world.
-   **Gallery Page**: Displays a gallery of popular travel destinations with reviews and ratings.
-   **Dynamic Content Management**: The featured places and gallery items are stored in a JSON file, making it easy to update and manage the content.

* * * * *

**Setup Instructions**
----------------------

### **1\. Prerequisites**

-   Python (version 3.8 or above)
-   Django (version 4.x or above)
-   A virtual environment tool (e.g., `venv`)
-   Git (for version control)
-   Basic understanding of HTML/CSS for frontend adjustments

### **2\. Clone the Repository**

Start by cloning the repository from GitHub:

bash

Copy code

`git clone <repository-url>
cd <repository-directory>`

### **3\. Setting Up the Virtual Environment**

It's a good practice to use a virtual environment to manage your dependencies:

bash

Copy code

`python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate``

### **4\. Install Required Dependencies**

Install the necessary Python packages listed in `requirements.txt`:

bash

Copy code

`pip install -r requirements.txt`

### **5\. Django Setup**

Before starting the Django server, you'll need to configure the project:

-   **Database Configuration**: If you're using SQLite (default), there are no additional setup steps required. If using another database like PostgreSQL, you'll need to configure your database settings in `settings.py`.

-   **Run Migrations**:

bash

Copy code

`python manage.py migrate`

-   **Create a Superuser** (to access the Django Admin):

bash

Copy code

`python manage.py createsuperuser`

-   **Static Files**: Ensure that your static files are collected and accessible:

bash

Copy code

`python manage.py collectstatic`

-   **Run the Development Server**:

bash

Copy code

`python manage.py runserver`

You can now view the project by going to `http://localhost:8000` in your browser.

* * * * *

**Project Folder Structure**
----------------------------

plaintext

Copy code

`/project_folder
    /app_name                # The main Django app
        /migrations          # Django migrations folder
        /templates           # HTML files for the pages
            /pages
                home.html
                gallery.html
        /static              # Static files (CSS, JS, images)
            /css
            /js
            /images
    /public                  # Stores external data (JSON)
        places.json          # JSON file with featured and gallery data
    manage.py                # Django management script
    settings.py              # Project configuration
    urls.py                  # Routing for the application`

### **Explanation of Key Files**

-   **`places.json`**: This JSON file holds the data for both featured places and gallery items. It is stored in the `public` folder and is loaded into views dynamically.
-   **`home.html`**: The homepage template that displays the featured places.
-   **`gallery.html`**: The gallery page template that displays popular destinations.
-   **`views.py`**: The Django views that load data from `places.json` and render it on the respective HTML pages.
-   **`settings.py`**: Django project settings, including database setup, static file management, and more.
-   **`urls.py`**: Routes that map URLs to the appropriate views.

* * * * *

**Key Changes and Updates**
---------------------------

### **1\. Data Separation**

-   The lists of `featured_places` and `gallery_places` have been moved to a separate JSON file (`places.json`) for easier content management. The JSON file can be modified without changing the Python code, and the data is loaded dynamically in the views.

### **2\. Dynamic Data Loading**

-   The `views.py` file has been updated to load content dynamically from the `places.json` file, ensuring that both the homepage and gallery page display the latest content without requiring database queries.

### **3\. Static File Handling**

-   Images, CSS, and JavaScript files are stored in the `static` folder, with correct paths configured in the `settings.py` file.

* * * * *

**Further Customization**
-------------------------

### **1\. Adding New Featured Places**

To add new featured places to the homepage, update the `featured_places` list inside the `places.json` file. Add new entries in the following format:

json

Copy code

`{
  "image": "path_to_image",
  "name": "Place Name",
  "des": "Description"
}`

### **2\. Adding New Gallery Items**

To add new items to the gallery, modify the `gallery_places` list in the `places.json` file. The format should follow this pattern:

json

Copy code

`{
  "image": "path_to_image",
  "name": "Place Name",
  "reviews": 400,
  "rating": 4.5,
  "des": "Description"
}`

### **3\. Working with the Django Admin**

To manage the project through Django's built-in admin interface, ensure you have a superuser account. You can then access the admin dashboard by navigating to `http://localhost:8000/admin` after logging in with your credentials.

* * * * *

**Best Practices**
------------------

-   **Version Control**: Always make sure to use Git or another version control system to track changes and collaborate with other developers.
-   **Virtual Environments**: Keep your environment isolated to avoid dependency conflicts.
-   **Security**: For production environments, make sure to configure security settings, such as setting `DEBUG = False` and using secure databases.

* * * * *
@https://euangoddard.github.io/clipboard2markdown/
**Conclusion**
--------------

This project has been designed with scalability and ease of content management in mind. By moving the featured places and gallery data to a JSON file, you can quickly update the content without modifying the Django backend code. Follow the setup instructions carefully, and you will have the project running in no time. For future developers, this structure allows for easy extensibility, whether through adding new pages, connecting to databases, or improving the frontend design.
