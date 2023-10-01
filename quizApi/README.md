# Quiz API

Quiz Api with lessons and user authentication and user stats

## Table of Contents

- [Introduction](#introduction)
- [Models](#models)
- [Serializers](#serializers)
- [Views](#views)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

## Introduction

Provide a brief introduction to your project. Explain its purpose, goals, and any relevant context. Mention any technologies or frameworks you have used.

## Models

### Lesson

- `title`: CharField with a maximum length of 255 characters, representing the title of a lesson.

### Question

- `lesson`: ForeignKey related to the `Lesson` model, establishing a relationship between questions and lessons.
- `is_multiple`: BooleanField, indicating whether the question allows multiple choices. Default is set to `True`.
- `text`: TextField, storing the text of the question.

### Choice

- `question`: ForeignKey related to the `Question` model, linking choices to questions.
- `text`: CharField with a maximum length of 255 characters, storing the text of a choice.
- `is_correct`: BooleanField, indicating whether the choice is correct. Default is set to `False`.

### User (Custom User Model)

This model extends the built-in `AbstractUser` model provided by Django, allowing you to add custom fields and behavior to user profiles.

### QuizResult

- `user`: ForeignKey related to the `User` model, associating quiz results with users.
- `lesson`: ForeignKey related to the `Lesson` model, connecting quiz results to specific lessons.
- `date`: DateTimeField, recording the date and time of the quiz result. Default is set to the current time using `timezone.now()`.
- `score`: FloatField, storing the user's score for the quiz.

### Signals

The code at the bottom of this file defines a signal handler that updates the `is_multiple` field of a `Question` when a `Choice` is saved or deleted. This ensures that the `is_multiple` field accurately represents whether a question has multiple correct choices.

## Serializers

### ChoiceSerializer

- `id`: IntegerField (read-only)
- `text`: CharField with a maximum length of 255 characters (required)
- `is_correct`: BooleanField (required)

### QuestionSerializer

- `id`: IntegerField (read-only)
- `text`: CharField with a maximum length of 255 characters (required)
- `choices`: ChoiceSerializer (many=True, required)
- `is_multiple`: BooleanField with a default value of `False` (optional)

### LessonSerializer

- `id`: IntegerField (read-only)
- `title`: CharField with a maximum length of 255 characters (required)
- `questions`: QuestionSerializer (many=True, required)

### SubmitAnswersSerializer

- `lesson_id`: IntegerField
- `answers`: DictField

### QuizResultSerializer

This serializer is based on the `QuizResult` model and automatically generated from the model's fields.

## Views

### LoginAPIView

- Endpoint: `/api/login/`
- Description: Handles user authentication using token-based authentication.
- Method: `POST`
- Parameters: `username`, `password`
- Returns: A token if authentication is successful, or an error message.

### RegistrationAPIView

- Endpoint: `/api/register/`
- Description: Allows users to register by providing a username, password, and email.
- Method: `POST`
- Parameters: `username`, `password`, `email`
- Returns: A token if registration is successful, or an error message.

### LogoutAPIView

- Endpoint: `/api/logout/`
- Description: Logs out the authenticated user.
- Method: `POST`
- Returns: A success message upon successful logout.

### LessonListView

- Endpoint: `/api/lessons/`
- Description: Lists all lessons.
- Method: `GET`
- Returns: A list of lessons serialized using `LessonSerializer`.

### CreateLessonFromJSON

- Endpoint: `/api/create_lesson/`
- Description: Creates a new lesson and related objects from JSON data.
- Method: `POST`
- Parameters: JSON data containing lesson details and questions.
- Returns: A success message upon successful creation.

### SubmitAnswersView

- Endpoint: `/api/submit_answers/`
- Description: Allows users to submit quiz answers for evaluation.
- Method: `POST`
- Parameters: `lesson_id`, `answers`
- Returns: The user's score for the submitted answers.

### UserQuizStatsView

- Endpoint: `/api/user_quiz_stats/`
- Description: Retrieves statistics on a user's quiz performance.
- Method: `GET`
- Returns: Statistics such as highest score, lowest score, average score, total attempts, and score variance.

### UserQuizRankingsView

- Endpoint: `/api/user_quiz_rankings/`
- Description: Retrieves rankings of users based on their quiz scores.
- Method: `GET`
- Returns: A list of user rankings based on average quiz scores.

## Getting Started

Explain how to set up your project locally for development.

### Prerequisites

List any software or dependencies that users need to have installed before they can run your project. Include links to where they can obtain these prerequisites.

### Installation

Provide step-by-step instructions for installing and configuring your project locally.

1. Clone the repository:
   ```shell
   git clone https://github.com/yourusername/your-project.git
   ```
