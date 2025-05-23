#  Flask REST API with PostgreSQL, JWT Authentication, and pgAdmin 

This is a Dockerized Flask REST API project that includes user registration, login, protected routes using JWT authentication, and PostgreSQL as the backend database. pgAdmin is included for managing the database via GUI.

---

# JWT Authorization Overview
JWT (JSON Web Token) is a compact, URL-safe means of representing claims between two parties. In this project, JWT is used for secure user authentication and authorization. After a successful login, the server generates a token that encodes the user's identity and permissions. This token is sent to the client and must be included in subsequent requests to access protected routes. The server validates the token to authorize access, ensuring stateless and secure communication between client and server.

![JWT Workflow](images/JWT.svg)



##  Project Structure

```
Project/
│
├── .env
├── app.py
├── routes/
│   ├── auth_routes.py
│   └── protected_routes.py
├── extensions.py
├── config.py
├── models.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

##  Features

-  JWT Authentication
-  User Registration and Login
-  Protected Routes
-  PostgreSQL Database
-  pgAdmin Interface for managing PostgreSQL
-  Docker + Docker Compose for containerization

---

##  Prerequisites

- Docker & Docker Compose installed
- Git installed
- Python (only for local development)

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create `.env` File

```env
DATABASE_URL=postgresql://<POSTGRES_USER>:<POSTGRES_PASSWORD>@<your hostname>:5432/<POSTGRES_DB>
JWT_SECRET_KEY=your_very_secret_key
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin123
```

### 3. Build and Run the Containers

```bash
docker-compose up --build
```

- Flask app: [http://localhost:5000](http://localhost:5000)
- pgAdmin: [http://localhost:5050](http://localhost:5050)

---

##  Accessing pgAdmin

1. Go to `http://localhost:5050`
2. Login:
   - **Email:** `admin@admin.com`
   - **Password:** `admin123`
3. Add a new server:
   - **Name:** `Postgres`
   - **Host name/address:** `your hostname`
   - **Port:** `5432`
   - **Username:** `<your username>`
   - **Password:** `<your password>`

---

##  Testing API Endpoints (via Postman)

###  Registration

```
POST /auth/register
{
  "username": "testuser",
  "password": "testpass"
}
```

###  Login

```
POST /auth/login
{
  "username": "testuser",
  "password": "testpass"
}
```

###  Protected Route

```
GET /protected/dashboard
Headers:
  Authorization: Bearer <JWT_TOKEN>
```

###  Logout

```
POST /auth/logout
Headers:
  Authorization: Bearer <JWT_TOKEN>
```

---

##  Clean Up

```bash
docker-compose down -v
```

---

##  Testing API Endpoints (via terminal)

###  Registration

```
curl -X POST http://127.0.0.1:5000/auth/register \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass"}'
```
### output

```
{"msg":"User registered successfully"}
```
### Login

```
curl -X POST http://127.0.0.1:5000/auth/login \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass"}'
```
### Output
```
{"access_token": "<JWT_TOKEN_HERE>"}
```
### Protected Login
```
curl -X GET http://127.0.0.1:5000/protected/dashboard \
-H "Authorization: Bearer <JWT_TOKEN_HERE>"

```
### Output
```
{"message":"Welcome testuser, this is your dashboard"}
```
### Logout
```
curl -X POST http://127.0.0.1:5000/auth/logout \
-H "Authorization: Bearer <JWT_TOKEN_HERE>"
```
### Output
```
{"msg":"Successfully logged out"}
```

##  License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

