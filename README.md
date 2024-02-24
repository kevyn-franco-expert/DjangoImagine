# Task Management API

Welcome to the Task Management API, a simple yet powerful system for managing tasks with multiple states. This API
allows you to create, list, update, delete, and change the status of tasks.

## API Endpoints

Below are the available endpoints, along with the HTTP methods, the required data to send, and the expected responses.

### Create a Task

- **Endpoint:** `/api/tasks/`
- **Method:** `POST`
- **Data Required:**

  ```json
  {
    "title": "Task Title",
    "description": "Task Description",
    "state": "New" // State must be one of the following: NEW, INPROGRESS, INREVIEW, COMPLETED
  }
  ```

- **Expected Success Response:** `HTTP 201 Created`
- **Expected Error Response:** `HTTP 400 Bad Request` (if data is invalid)

### List All Tasks

- **Endpoint:** `/api/tasks/`
- **Method:** `GET`
- **Expected Success Response:** `HTTP 200 OK` with a list of tasks.

### Update a Task

- **Endpoint:** `/api/tasks/<id>/`
- **Method:** `PUT`
- **Data Required:**

  ```json
  {
    "title": "Updated Title",
    "description": "Updated Description",
    "state": "In Progress"
  }
  ```

- **Expected Success Response:** `HTTP 200 OK`
- **Expected Error Response:** `HTTP 404 Not Found` (if task with the given ID does not exist)

### Delete a Task

- **Endpoint:** `/api/tasks/<id>/`
- **Method:** `DELETE`
- **Expected Success Response:** `HTTP 204 No Content`
- **Expected Error Response:** `HTTP 404 Not Found` (if task with the given ID does not exist)

### Change Task State

- **Endpoint:** `/api/tasks/<id>/change_state/`
- **Method:** `PATCH`
- **Data Required:**

  ```json
  {
    "state": "Completed" // State must be one of the following: NEW, INPROGRESS, INREVIEW, COMPLETED
  }
  ```

- **Expected Success Response:** `HTTP 200 OK`
- **Expected Error Response:** `HTTP 400 Bad Request` (if the state is invalid)

## Running the Application

To run the application, make sure you have Docker installed and follow these steps:

1. Clone the repository to your local machine.
2. chmod +x entrypoint.sh in the directory of the project.
2. Navigate to the root directory of the project.
3. Run `docker-compose build` to build and start the containers.
3. docker-compose run web python manage.py makemigrations manages
4. docker-compose run web python manage.py migrate
4. docker-compose run web python manage.py createsuperuser
3. Run `docker-compose up` to build and start the containers.
4. The API will be available at `http://localhost:8000/api/tasks/`.
4. Check API on Swagger `http://localhost:8000/swagger/`.

## Testing the Application

Unit and integration tests are provided to ensure the API works as expected. To run the tests, follow these steps:

1. Ensure your Docker containers are up and running.
2. Execute `docker-compose exec web python manage.py test api`.

Replace `api` with the name of your Django app where the tests reside.

# Project Architecture Overview

## Models

### Task Model:

- `Task`: The central model representing tasks.
    - `title`: A CharField storing the task's title.
    - `description`: A TextField for detailed task description.
    - `created_at`: A DateTimeField automatically capturing the creation time.
    - `state`: A CharField with choices like 'NEW', 'INPROGRESS', 'INREVIEW', 'COMPLETED', representing the task's
      current state.

This model is designed for straightforward task tracking and management, with a focus on clarity and functionality.

## API Endpoints

### TaskViewSet:

- Provides comprehensive RESTful endpoints using Django's `viewsets.ModelViewSet`.
    - Retrieve: Get a specific task by ID.
    - List: List all tasks.
    - Create: Add a new task.
    - Update: Modify an existing task.
    - Partial Update: Partially update a task.
    - Destroy: Delete a task.

Each method is documented with `swagger_auto_schema` for enhanced clarity and usability in Swagger's interactive
documentation.

## Serializer

### TaskSerializer:

- A subclass of `serializers.ModelSerializer` linked to the Task model.
    - Fields: `id`, `title`, `description`, `created_at`, `state`.

This serializer facilitates the conversion of task data to and from JSON format, ensuring adherence to the defined model
structure for HTTP request and response handling.

## Contributing

Contributions to the Task Management API are welcome. Please fork the repository and submit a pull request with your
proposed changes or improvements.

## License

This project is licensed under the [MIT License](LICENSE.md).
