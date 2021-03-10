# User Management

This project is developed for creating REST APIS based on Django.

It contains:  

1. Sign Up/Forgot Password Apis

2. JWT Authentication

3. 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Used
internal Django Groups to achieve the same).

4. Teacher has persmissions to add or list the students

5. Super User has persmission to add/list every user in database

6. Students only able to see his/her information only.

## **Tech Stack Used**

* [Django](https://www.djangoproject.com/): Django builds better web apps with less code
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Rest APIs with Django
* Database used: [SQLite](https://www.sqlite.org/index.html) (for local testing), [PostgreSQL](https://www.psycopg.org/)


## **Create a Super User(Admin)**

Run the following command and enter the prompted user fields like username, email and password

```js
$ python manage.py createsuperuser
```

Enter your desired username and press enter.

```js
Username: admin
```

You will then be prompted for your desired email address:

```js
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```js
Password: **********
Password (again): *********
Superuser created successfully.
```

## **API ENDpoints**

> ### For Teacher SignUp

* HTTP Method - **POST**

* Endpoint - **`/teacher_signup/`**

* Json Body contains these inputs - first_name, last_name, username, email, passowrd

Example Request:

```js
curl --location --request POST 'http://localhost:8000/teacher_signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
"first_name": "xyz",
"last_name": "abc",
"email": "abc@gmail.com",
"username": "xyz",
"password": "****"
}'
```

Sample Response:

```json
{
    "username": "xyz",
    "access": "xxxxx",
    "refresh": "xxxxx",
}
```

> ### For Student SignUp

* HTTP Method - **POST**

* Endpoint - **`/student_signup/`**

* Json Body contains these inputs - first_name, last_name, username, email, passowrd

Example Request:

```js
curl --location --request POST 'http://localhost:8000/teacher_signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
"first_name": "xyz",
"last_name": "abc",
"email": "abc@gmail.com",
"username": "xyz",
"password": "****"
}'
```

Sample Response:

```json
{
    "username": "xyz",
    "access": "xxxxx",
    "refresh": "xxxxx",
}
```

> ### For viewing the Student List

* HTTP Method - **GET**

* Endpoint - **`/student_list/`**

* Request needs JWT Authentication


    If access token is valid:

    ```js
    http http://127.0.0.1:8000/student_list/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"
    ```

    If access token has expired, generate new access token using refresh token as

    ```js
    http post http://127.0.0.1:8000/api/token/refresh/ refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMwODIyMiwianRpIjoiNzAyOGFlNjc0ZTdjNDZlMDlmMzUwYjg3MjU1NGUxODQiLCJ1c2VyX2lkIjoxfQ.Md8AO3dDrQBvWYWeZsd_A1J39z6b6HEwWIUZ7ilOiPE
    ```

Sample Response:

```json
 [
    {
        "first_name": "xyz",
        "last_name": "abc",
        "email": "abc@gmail.com",
        "username": "xyz",
        "password": "****"
    },
    {
        "first_name": "xyz",
        "last_name": "abc",
        "email": "abc@gmail.com",
        "username": "xyz",
        "password": "****"
    }
 ]
```

> ### For adding a Student

* HTTP Method - **POST**

* Endpoint - **`/student_list/`**

* Request needs JWT Authentication


    If access token is valid:

    ```js
    http http://127.0.0.1:8000/student_list/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"
    ```

    If access token has expired, generate new access token using refresh token as

    ```js
    http post http://127.0.0.1:8000/api/token/refresh/ refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMwODIyMiwianRpIjoiNzAyOGFlNjc0ZTdjNDZlMDlmMzUwYjg3MjU1NGUxODQiLCJ1c2VyX2lkIjoxfQ.Md8AO3dDrQBvWYWeZsd_A1J39z6b6HEwWIUZ7ilOiPE
    ```

Example Request:

```js
curl --location --request POST 'http://localhost:8000/student_list/' \
--header 'Content-Type: application/json' \
--data-raw '{
"first_name": "xyz",
"last_name": "abc",
"email": "abc@gmail.com",
"username": "xyz",
"password": "****"
}'
```

Sample Response:

```json
{
    "username": "xyz",
    "access": "xxxxx",
    "refresh": "xxxxx",
}
```

> ### For viewing the Student Detail

* HTTP Method - **GET**

* Endpoint - **`/student_detail/`**

* Request needs JWT Authentication


    If access token is valid:

    ```js
    http http://127.0.0.1:8000/student_detail/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"
    ```

    If access token has expired, generate new access token using refresh token as

    ```js
    http post http://127.0.0.1:8000/api/token/refresh/ refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMwODIyMiwianRpIjoiNzAyOGFlNjc0ZTdjNDZlMDlmMzUwYjg3MjU1NGUxODQiLCJ1c2VyX2lkIjoxfQ.Md8AO3dDrQBvWYWeZsd_A1J39z6b6HEwWIUZ7ilOiPE
    ```

Sample Response:

```json
{
    "first_name": "xyz",
    "last_name": "abc",
    "email": "abc@gmail.com",
    "username": "xyz",
    "password": "****"
}
```

### For Resetting Password

If password has to be resetted, the following end points will be viewed in order.

* HTTP Method - **POST**

* Endpoint - **`/api/password_reset/`**


The user will enter email where a token will be received. For the development, the token will be received in the backend.

Get the token and then do the proceed to following endpoint>

* HTTP Method - **POST**

* Endpoint - **`/api/password_reset/confirm/`**

The user will enter the new password and the token received on the mail or say backend.

Sample Response:

```json
{
    "status": 200
}
```
