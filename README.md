# Recipe Management App

This is a recipe management application that allows users to create and modify recipes, search for recipes by ingredient, and automatically rate recipes based on their difficulty level. The application is built using Python 3.6+ and Django 3 and utilizes an SQLite database during development, with the option to connect to a PostgreSQL database for production.

## User Goals

- Create and modify recipes
- Search for recipes by ingredient
- View detailed information about each recipe
- Automatically calculate and display the difficulty level of recipes
- Add user recipes to the database
- Use a Django Admin dashboard for managing database entries
- Access statistics and visualizations based on trends and data analysis

## Key Features

- User authentication: Users can register, login, and logout from the application.
- Recipe search: Users can search for recipes based on ingredients.
- Automatic rating: Recipes are rated based on their difficulty level, which is calculated by the application.
- Error handling: The application handles exceptions and displays user-friendly error messages.
- Recipe details: Users can view additional details about each recipe if desired.
- Database integration: User recipes are stored in an SQLite database during development, with the option to use a PostgreSQL database in production.
- Django Admin dashboard: The application includes a dashboard for managing database entries.
- Statistics and visualizations: The application provides statistics and visualizations based on recipe trends and data analysis.

## Technical Requirements

- Python 3.6+ and Django 3 installations.
- Exception handling: The application handles errors that occur during user input and displays user-friendly error messages.
- Database connectivity: The application connects to a PostgreSQL database hosted locally on the same system for production. During development, an SQLite database is used.
- User-friendly interface: The application provides an intuitive and easy-to-use interface with simple forms of input and clear instructions. Login and logout menus are presented neatly with concise prompts.
- Proper documentation and tests: The code is thoroughly documented and includes automated tests. The project is uploaded to GitHub, along with a "requirements.txt" file containing the necessary modules.
- Readme file: A readme file is provided with instructions on how to download and run the application locally on any machine.

## Installation and Setup

To run the application locally, follow these steps:

1.  Ensure Python 3.6+ and Django 3 are installed on your machine.
2.  Clone the project repository from GitHub.
3.  Install the required modules by running `pip install -r requirements.txt` in your terminal.
4.  Set up the database configuration in the project's settings file. For development, use SQLite. For production, configure PostgreSQL.
5.  Run the database migrations using the command `python manage.py migrate`.
6.  Start the development server with the command `python manage.py runserver`.
7.  Access the application by opening a web browser and navigating to `http://localhost:8000`.

For detailed instructions on deploying the application in a production environment or using the Django Admin dashboard, refer to the documentation included in the project.
