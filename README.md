# LogMate — Internal Activity Logging Tool

LogMate is a **web-based internal logging system** built with Django to track daily work activities and professional interactions.
It was designed to replace manual note-taking with a **structured, searchable, and auditable logging workflow**.

The application focuses on **accountability, traceability, and process discipline** rather than public-facing features.

---

## Problem Statement

In a non-technical operational role, maintaining accountability for daily tasks and important interactions required consistent manual logging, which was inefficient and error-prone.

LogMate solves this by providing:

* Structured data capture
* Centralized records
* Time-based filtering for reviews and audits

---

## Core Features

* **Structured Activity Logging**

  * Date and time
  * Interaction context (in-person / call / message)
  * Person involved
  * Department (ForeignKey-based)
  * Status tracking (PENDING / COMPLETED)
  * Action and guidance notes

* **Relational Data Modeling**

  * Department managed as a separate entity
  * Controlled status choices to enforce consistency

* **Log Management**

  * View all logs with detailed records
  * Update and delete existing logs
  * Filter logs by:

    * Today
    * Last 7 days
    * Last 30 days

* **Server-Rendered UI**

  * Django templates
  * Clean form handling and validation

---

## Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Django Templates)
* **Database:** PostgreSQL
* **Deployment:** Render

---

## Application Structure (High Level)

* Models define structured logging and department relationships
* Views handle CRUD workflows and filtered queries
* Templates render list views, detail views, and forms
* Deployed as a single Django service with environment-based configuration

---

## Deployment

The application is deployed on Render.

**Live Demo:**
[https://logmate-rrst.onrender.com](https://logmate-rrst.onrender.com)

---

## Intended Scope

* Single-user internal tool
* Designed for personal operational accountability
* Not intended as a multi-tenant or public SaaS application

---

## Author

Developed and maintained by **Pratik Atul Gaikwad**.

---

## License

This project is intended for learning and internal use.
