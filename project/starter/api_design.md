# Module 4 Project — Part 2: Study Tracker API Design

Jordan Hill
10/10/2026

---

## The App: Study Tracker


The Study Tracker API allows students to manage their courses, record study sessions, and set weekly study goals. Students can track how much time they spend studying each course and compare their progress against their goals. The API provides endpoints for creating, viewing, updating, and deleting study related information.


---

## Section 1 — Resources

| Resource | Key Attributes |
|----------|----------------|
| Students | id, name, email |
| Courses | id, student_id, name, description |
| Study Sessions | id, student_id, course_id, duration_minutes, notes, studied_at |
| Goals | id, student_id, course_id, target_hours, week_start |


---

## Section 2 — Relationships

- Student - Course: One student can have many courses, but each course belongs to one student (one-to-many).
- Student - Study Session: One student can log many study sessions, but each session belongs to one student (one-to-many).
- Course - Study Session: One course can have many study sessions, but each session belongs to one course (one-to-many).
- Student - Goal: One student can set many weekly goals, but each goal belongs to one student (one-to-many).
- Course - Goal: One course can have many weekly goals, but each goal belongs to one course (one-to-many).


---

## Section 3 — Endpoints


| Method | URI | Description | Auth Required? |
|--------|-----|-------------|----------------|
| POST | /study_sessions | Create a new study session | Yes |
| GET | /study_sessions | List the student's study sessions | Yes |
| GET | /study_sessions/{id} | Get a specific study session | Yes |
| PUT | /study_sessions/{id} | Update a study session | Yes |
| DELETE | /study_sessions/{id} | Delete a study session | Yes |
| GET | /study_sessions?course_id={id} | Filter study sessions by course | Yes |
| POST | /courses | Create a course | Yes |
| GET | /courses | List the student's courses | Yes |
| GET | /courses/{id} | Get a specific course | Yes |
| PUT | /courses/{id} | Update a course | Yes |
| DELETE | /courses/{id} | Delete a course | Yes |
| POST | /goals | Create a weekly study goal | Yes |
| GET | /goals | List weekly study goals | Yes |
| PUT | /goals/{id} | Update a weekly study goal | Yes |
| GET | /goals/{id} | Retrieve a specific weekly study goal | Yes |
| GET | /students/{id}/progress | View a student's study progress | Yes |


---

## Section 4 — Request/Response Schemas

### POST /study_sessions — Create a new session

REQUEST:

```json
{
    "course_id": 3,
    "duration_minutes": 90,
    "notes": "Practiced Python REST APIs",
    "studied_at": "2026-10-10T14:00:00Z"
}
```

RESPONSE (201 Created):

```json
{
    "id": 12,
    "student_id": 5,
    "course_id": 3,
    "duration_minutes": 90,
    "notes": "Practiced Python REST APIs",
    "studied_at": "2026-10-10T14:00:00Z"
}
```

### GET /students/{id}/progress

RESPONSE (200 OK):

```json
{
        "student_id": 5,
        "total_study_minutes": 720,
        "courses": [
            {
            "course_id": 3,
            "course_name": "Python",
            "studied_hours_this_week": 8,
            "weekly_goal_hours": 10,
            "goal_met": false
            },
            {
            "course_id": 4,
            "course_name": "SQL",
            "studied_hours_this_week": 4,
            "weekly_goal_hours": 4,
            "goal_met": true
        }
    ]
}
```

### POST /goals

REQUEST:

```json
{
    "course_id": 3,
    "target_hours": 15,
    "week_start": "2026-10-12"
}
```

RESPONSE (201 Created):

```json
{
    "id": 8,
    "student_id": 5,
    "course_id": 3,
    "target_hours": 15,
    "week_start": "2026-10-12"
}
```


### GET /study_sessions/{id}

RESPONSE (200 OK):

```json
{
    "id": 12,
    "student_id": 5,
    "course_id": 3,
    "duration_minutes": 90,
    "notes": "Practiced Python REST APIs",
    "studied_at": "2026-10-10T14:00:00Z"
}
```
---

## Section 5 — Authentication

| Endpoint | Auth Required | Notes |
|----------|---------------|-------|
| GET /courses | Yes | Students can view only their own courses |
| POST /study_sessions | Yes | Students can create sessions only for their own courses |
| GET /students/{id}/progress | Yes | Students can view only their own progress |
| DELETE /study_sessions/{id} | Yes | Only the session owner can delete it |


**Auth method and rationale:**
The Study Tracker API uses JWT Bearer token authentication. Students must log in to receive a token, which is included in the Authorization header for protected requests.

All study related endpoints require authentication because courses, study sessions, goals, and progress contain personal information.

Students can only view, create, update, or delete resources belonging to their own accounts. The server verifies resource ownership before allowing changes.

Invalid or missing tokens return HTTP 401 Unauthorized. Authenticated users attempting to access another student's protected resources receive HTTP 403 Forbidden.


---

## Section 6 — Error Responses for POST /study_sessions

| Status Code | When it occurs |
|-------------|----------------|
| 201 | Created: The study session was successfully saved. |
| 400 | Bad Request: The request contains malformed JSON or invalid syntax. |
| 401 | Unauthorized: The JWT token is missing, expired, or invalid. |
| 403 | Forbidden: The student attempts to log a session for a course they do not own. |
| 404 | Not Found: The specified course_id does not exist. |
| 422 | Unprocessable Content: Required fields are missing or values fail validation, such as a negative duration_minutes. |
| 500 | Internal Server Error: An unexpected server-side error prevents the session from being created. |


