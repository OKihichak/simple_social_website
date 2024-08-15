# 🌐 SimpleSocial

📝 **Contents**
- [Introduction](#introduction)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Running the Project](#running-the-project)
- [API Key Management](#api-key-management)
- [Contributing](#contributing)
- [Contact Information](#contact-information)

## 🌟 Introduction
**SimpleSocial** is a Django-based social networking application that allows users to create and manage posts, join groups, and interact with other users. The project is structured into multiple Django apps to handle different functionalities like user authentication, group management, and posting.

## 💻 Technology Stack
- **Django**: The web framework used to build the application.
- **Bootstrap 3**: Used for responsive design and styling.
- **SQLite**: The default database used for local development.
- **Django Authentication**: Handles user authentication and session management.
- **HTML, CSS, JavaScript**: Front-end technologies for building the user interface.

## 👀 Features
- **User Authentication**: Sign up, login, and logout functionalities.
- **Post Management**: Create, view, and delete posts.
- **Group Management**: Join, leave, and create user groups.
- **Responsive Design**: Accessible on various devices with a responsive UI.

## 🗂️ Project Structure
- **`accounts/`**: Handles user authentication.
  - **`templates/accounts/login.html`**: Login page template.
  - **`templates/accounts/signup.html`**: Sign-up page template.
  
- **`groups/`**: Manages groups and memberships.
  - **`templates/groups/group_list.html`**: Lists all groups.
  - **`templates/groups/group_detail.html`**: Shows details of a specific group.
  - **`templates/groups/group_form.html`**: Group creation form.
  
- **`posts/`**: Manages posts.
  - **`templates/posts/post_list.html`**: Lists all posts.
  - **`templates/posts/post_detail.html`**: Shows details of a specific post.
  - **`templates/posts/post_form.html`**: Post creation form.
  
- **`simplesocial/`**: Main Django project directory.
  - **`settings.py`**: Django settings for the project.
  - **`urls.py`**: URL routing configuration.
  - **`views.py`**: View functions and class-based views.

- **`static/`**: Contains static assets such as CSS, JavaScript, and images.
  - **`master.css`**: Custom styles for the project.
  - **`master.js`**: Custom JavaScript for the project.

- **`templates/`**: Shared HTML templates.
  - **`base.html`**: Base template extended by other templates.
  - **`index.html`**: Homepage template.

## 🚀 Running the Project
To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/simplesocial.git
    cd simplesocial
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations to set up the database:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:** Open your web browser and navigate to `http://localhost:8000`.

## 🔑 API Key Management
Since the project doesn't directly involve external APIs requiring keys, standard Django secret management practices should be followed:
- Keep the `SECRET_KEY` in the `settings.py` file secure.
- Consider using environment variables or Django's `django-environ` package for managing sensitive information in production.

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute to the SimpleSocial project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature/YourFeatureName
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -m 'Add YourFeatureName'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature/YourFeatureName
    ```
5. **Open a pull request** to discuss and merge your changes.

## 📧 Contact Information
- **Email**: artem.burov0205@gmail.com
- **GitHub**: [Oleh Kihichak](https://github.com/OKihichak)
