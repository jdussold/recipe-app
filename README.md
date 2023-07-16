# Recipe Management App

This is a recipe management application that allows users to create, modify, and discover a wide range of recipes. With its user-friendly interface and powerful features, the app simplifies the process of organizing and exploring recipes. Whether you're a cooking enthusiast or a professional chef, this app provides a seamless experience for managing your culinary creations.

## User Goals

- **Create and Modify Recipes**: Users can easily create new recipes and make modifications to existing ones. The app provides a comprehensive form where users can enter recipe details such as title, cooking time, description, and ingredients. The recipes can be edited at any time to add or remove ingredients, update cooking instructions, or make any other desired changes.

- **Search for Recipes by Ingredient**: The app offers a convenient search functionality that allows users to find recipes based on specific ingredients. Users can simply enter the ingredient they have on hand, and the app will display a list of matching recipes. This feature is particularly helpful for users looking to make use of ingredients in their pantry or fridge.

- **View Detailed Recipe Information**: Users can access detailed information about each recipe, including the title, cooking time, description, and ingredients. This allows users to get a complete understanding of the recipe before deciding to try it out. The app provides an organized and visually appealing display of recipe details to enhance the user experience.

- **Automatic Recipe Rating**: The app automatically rates recipes based on their difficulty level. The difficulty level is calculated by considering factors such as cooking time and the number of ingredients. Users can quickly identify easy, medium, intermediate, or hard recipes based on the ratings. This feature helps users choose recipes that match their skill level and available time.

- **Add User Recipes to the Database**: The app allows users to contribute their own recipes to the recipe database. Users can easily add their recipes, including all the necessary details and ingredients. By sharing their culinary creations with the community, users can inspire others and contribute to the growing collection of recipes.

- **Django Admin Dashboard**: The app includes a Django Admin dashboard, which provides a user-friendly interface for managing database entries. With the dashboard, administrators can efficiently add, edit, and delete recipes, ingredients, and other related data. This feature simplifies the administrative tasks and ensures smooth operation of the app.

- **Access Statistics and Visualizations**: The app goes beyond basic recipe management by offering statistics and visualizations based on recipe trends and data analysis. Users can gain insights into popular ingredients, most-rated recipes, and other interesting patterns. These insights can help users discover new recipes, identify cooking trends, and make informed decisions in their culinary endeavors.

- **Database Connectivity and Design**: The app connects to a PostgreSQL database for production. During development, an SQLite database is used. The database configuration can be easily set up in the project's settings file.

  The application has four main entities:

  - `User`
  - `Recipe`
  - `Ingredient`
  - `RecipeIngredient`

  Here are the tables representing these entities:

  ### User

  | Attribute | Type              |
  | --------- | ----------------- |
  | id        | Unique Identifier |
  | username  | String            |
  | password  | String            |

  ### Recipe

  | Attribute    | Type              |
  | ------------ | ----------------- |
  | id           | Unique Identifier |
  | user_id (FK) | Foreign Key       |
  | title        | String            |
  | description  | String            |
  | cooking_time | Integer           |
  | difficulty   | String            |

  ### Ingredient

  | Attribute | Type              |
  | --------- | ----------------- |
  | id        | Unique Identifier |
  | name      | String            |

  ### RecipeIngredient

  | Attribute          | Type              |
  | ------------------ | ----------------- |
  | id                 | Unique Identifier |
  | recipe_id (FK)     | Foreign Key       |
  | ingredient_id (FK) | Foreign Key       |
  | quantity           | Integer           |

## Technical Requirements

To run the application, ensure the following technical requirements are met:

- **Python 3.6+ and Django 3 installations**: The app is built using Python programming language and utilizes Django, a high-level web framework, for efficient development.

- **Exception Handling**: The application incorporates robust exception handling to gracefully handle errors that may occur during user input. It provides user-friendly error messages to guide users in resolving any issues.

- **Database Connectivity**: The app connects to a PostgreSQL database for production. During development, an SQLite database is used. The database configuration can be easily set up in the project's settings file.

- **User-Friendly Interface**: The app prioritizes user experience with an intuitive and easy-to-use interface. It offers simple forms of input, clear instructions, and neatly presented menus for login and logout.

- **Documentation and Tests**: The app is thoroughly documented, making it easy for developers to understand and modify the codebase. Additionally, it includes automated tests to ensure proper functionality. The project is uploaded to GitHub, along with a "requirements.txt" file containing the necessary modules.

## Installation and Setup

To run the application locally, follow these steps:

1. Ensure Python 3.6+ and Django 3 are installed on your machine.
2. Clone the project repository from GitHub.
3. Install the required modules by running `pip install -r requirements.txt` in your terminal.
4. Set up the database configuration in the project's settings file. For development, use SQLite. For production, configure PostgreSQL.
5. Run the database migrations using the command `python manage.py migrate`.
6. Start the development server with the command `python manage.py runserver`.
7. Access the application by opening a web browser and navigating to `http://localhost:8000`.
