# JudgeMe

JudgeMe is a social media web application built with Django. It allows users to register, log in, create posts with images and captions, and interact with other users' posts.

## Features

*   **User Authentication**: Multi-step user registration and login system.
*   **User Profiles**: Each user has a profile with a profile picture, bio, and other details.
*   **Create Posts**: Users can create posts with a caption and an image.
*   **Feed**: A home page that will display a feed of posts from other users.
*   **Like, Comment, Repost**: Users can interact with posts by liking, commenting, and reposting.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/JudgeMe.git
    ```
2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file in the root directory and add the following:**
    ```
    SECRET_KEY=your-secret-key
    DEBUG=True
    ```
5.  **Run the migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1.  Register for a new account by navigating to `/auth/register-step-one/`.
2.  Log in to your account at `/auth/login/`.
3.  Create a new post at `/post/create/`.
4.  View the main feed on the home page.

## Future Development

*   **AI Content Moderation**: Implement an AI-powered content moderation system to monitor and flag inappropriate content in posts and comments.
*   **Content Suggestions**: Provide users with personalized content suggestions based on their interests and interactions.
*   **Feed Algorithm**: Develop a more sophisticated feed algorithm to rank and display posts.
*   **Real-time Notifications**: Implement real-time notifications for likes, comments, and other interactions.
