# NayePankh Foundation

### AI-Powered Multimodal NGO Campaign and Volunteer Management Platform

---

## Live Demo

**Application URL**

https://upadhyeshraddha54-spec-nayepankh-ai-app-drn6k7.streamlit.app/

---

## Project Overview

NayePankh Foundation is a Multimodal AI-powered web application developed to assist Non-Governmental Organizations (NGOs) in planning, managing, and monitoring social impact campaigns efficiently.

The platform integrates Generative AI, Image Generation, Database Management, and Interactive Analytics into a single solution. It enables NGOs to automatically generate campaign content, create promotional posters, manage volunteers, and track organizational impact through a centralized dashboard.

The project demonstrates the practical application of Artificial Intelligence to solve real-world challenges faced by NGOs and community-driven organizations.

---

# Problem Statement

NGOs often face operational challenges such as:

* Creating engaging campaign content.
* Designing promotional materials.
* Managing volunteer registrations manually.
* Tracking campaign activities.
* Monitoring volunteer participation.
* Maintaining campaign records.
* Measuring organizational impact.

These activities generally require multiple tools and considerable manual effort.

NayePankh Foundation addresses these challenges through a unified AI-powered platform that automates campaign creation, volunteer management, and impact tracking.

---

# Objectives


The primary objectives of this project are:

* Automate NGO campaign planning.
* Generate campaign content using AI.
* Create campaign posters automatically.
* Digitize volunteer registration.
* Maintain campaign records efficiently.
* Provide campaign analytics and insights.
* Improve NGO operational efficiency.
* Demonstrate the use of Multimodal Generative AI in social impact initiatives.

---

# Multimodal AI Integration

NayePankh Foundation is designed as a Multimodal AI system that combines multiple data modalities into a single workflow.

## Text Generation

The application generates campaign-related content using Large Language Models (LLMs).

Generated content includes:

* Campaign Descriptions
* Awareness Messages
* Donor Appeals
* Volunteer Recruitment Content
* Community Engagement Messages
* Call-to-Action Statements

### Input Parameters

* Campaign Topic
* Location
* Event Date
* Event Time
* Venue

---

## Image Generation

The application automatically generates campaign posters using AI-powered text-to-image models.

Generated posters are based on:

* Campaign Theme
* Location
* Date
* Time
* Venue
* Social Impact Context

### Model Used

```text
black-forest-labs/FLUX.1-schnell
```

---

## Why It Is Multimodal

The application processes and generates multiple forms of information.

| Modality         | Purpose                          |
| ---------------- | -------------------------------- |
| Text             | Campaign Content Generation      |
| Images           | Campaign Poster Generation       |
| Structured Data  | Volunteer and Campaign Records   |
| Visual Analytics | Dashboard Insights and Reporting |

By combining AI-generated text, AI-generated visuals, structured database information, and analytics dashboards, the platform delivers a complete multimodal experience.

---

# Features

## 1. AI Campaign Generator

The Campaign Generator enables NGOs to create professional campaigns instantly.

### Supported Campaign Types

* Blood Donation Drive
* Food Distribution
* Cloth Donation
* Tree Plantation
* Women Empowerment
* Menstrual Hygiene Awareness
* Child Education Support
* Health Checkup Camp
* Animal Welfare Campaign
* Environmental Awareness
* Custom Campaigns

### Workflow

1. Select campaign type.
2. Select city.
3. Choose event date and time.
4. Enter venue details.
5. Generate campaign content using AI.
6. Save campaign data to the database.

### Generated Output

* Campaign Description
* Awareness Message
* Volunteer Appeal
* Donor Engagement Content
* Community Outreach Message

---

## 2. AI Poster Generation

The platform automatically generates promotional posters for NGO campaigns.

### Inputs

* Campaign Topic
* Location
* Date
* Time
* Venue

### AI Model

```text
black-forest-labs/FLUX.1-schnell
```

### Benefits

* Reduces manual design effort.
* Creates visually appealing promotional material.
* Enables rapid campaign deployment.

---

## 3. Volunteer Management System

The Volunteer Management module enables NGOs to register and manage volunteers.

### Information Collected

* Volunteer Name
* Email Address
* Phone Number
* City
* Skills
* Assigned Campaign

### Supported Skills

* Teaching
* Designing
* Photography
* Social Media Management
* Event Management
* Fundraising

### Validation Features

* Email validation using Regular Expressions
* Phone number validation
* Mandatory field checks
* Campaign availability validation

---

## 4. NGO Impact Dashboard

The Dashboard provides a centralized overview of campaign activities and volunteer engagement.

### Dashboard Metrics

* Total Campaigns
* Total Volunteers
* Today's Events
* Upcoming Campaigns

### Campaign Tracking

#### Upcoming Campaigns

Displays future campaigns.

#### Today's Campaigns

Displays campaigns scheduled for the current day.

#### Completed Campaigns

Displays previously conducted campaigns.

---

## 5. Volunteer Analytics

The platform provides campaign-wise volunteer analytics.

### Features

* Volunteer count per campaign
* Campaign participation tracking
* Volunteer engagement insights
* Visual analytics using charts

---

# Technology Stack

## Frontend

* Streamlit
* HTML
* CSS
* Custom UI Components

## Backend

* Python

## Database

* SQLite3

## Artificial Intelligence

* Hugging Face Inference API
* Large Language Models (LLMs)

## Image Generation

* Hugging Face Text-to-Image Models
* FLUX.1 Schnell

## Data Processing

* Regular Expressions (re)
* datetime
* sqlite3

---

# System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ├── Campaign Generator
 │       │
 │       ▼
 │   Content Agent
 │       │
 │       ▼
 │   Hugging Face API
 │
 ├── Poster Generator
 │       │
 │       ▼
 │   FLUX.1 Schnell
 │
 ├── Volunteer Management
 │       │
 │       ▼
 │   SQLite Database
 │
 └── NGO Dashboard
         │
         ▼
      Analytics Engine
```

---

# Project Structure

```text
NayePankh-AI/
│
├── app.py
├── database.py
├── content_agent.py
├── poster_generator.py
├── requirements.txt
├── README.md
│
└── ngo.db
```

---

# Database Design

## Campaign Table

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| topic    | TEXT    |
| location | TEXT    |
| date     | TEXT    |
| time     | TEXT    |
| venue    | TEXT    |
| content  | TEXT    |

---

## Volunteer Table

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| name     | TEXT    |
| email    | TEXT    |
| phone    | TEXT    |
| city     | TEXT    |
| skills   | TEXT    |
| campaign | TEXT    |

---

# AI Integration

## Content Generation

Campaign content is generated dynamically using Large Language Models through the Hugging Face Inference API.

### Generated Content

* Campaign Description
* Awareness Message
* Volunteer Appeal
* Donor Engagement Content
* Community Outreach Message

---

## Poster Generation

Campaign posters are generated using Text-to-Image AI models.

### Model

```text
black-forest-labs/FLUX.1-schnell
```

### API Provider

Hugging Face Inference API

---

# User Interface Design

The application features a modern dark-themed interface optimized for usability and accessibility.

### UI Components

* Hero Landing Page
* Interactive Feature Cards
* Responsive Layout
* Campaign Forms
* Volunteer Forms
* Dashboard Analytics
* Metric Cards
* Visual Charts

---

# Data Validation

The platform implements multiple validation mechanisms.

## Email Validation

Regular Expression-based validation ensures correct email formatting.

## Phone Number Validation

Validation checks:

* Numeric input only
* Exactly 10 digits

## Campaign Validation

* Mandatory venue entry
* Campaign availability checks

---

# Security Measures

* Input validation and sanitization
* Parameterized database operations
* Secure API key management using Streamlit Secrets
* Controlled user input handling

---

# Deployment

The application is deployed using Streamlit Community Cloud.

### Deployment Workflow

1. Source code hosted on GitHub.
2. Repository connected to Streamlit Cloud.
3. Environment configured.
4. Hugging Face API credentials added through Streamlit Secrets.
5. Automatic deployment enabled.

### Deployment Platform

* Streamlit Community Cloud

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/your-username/nayepankh-ai.git
```

## Navigate to Project Directory

```bash
cd nayepankh-ai
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# Unique Selling Points (USP)

* AI-Powered Campaign Creation
* Automated Poster Generation
* Multimodal AI Architecture
* End-to-End NGO Management Solution
* Volunteer Analytics Dashboard
* Real-Time Campaign Tracking
* Cloud-Based Deployment
* User-Friendly Interface
* Practical Social Impact Application

---

# Innovation Aspect

Unlike traditional NGO management systems that primarily focus on record keeping, NayePankh Foundation integrates Generative AI directly into campaign planning and outreach.

The platform enables organizations to:

* Generate campaign content instantly.
* Create promotional posters automatically.
* Manage volunteers efficiently.
* Track campaign performance.
* Analyze community engagement.

The combination of Generative AI, Multimodal Processing, Data Analytics, and NGO Operations Management makes the solution both innovative and practically applicable.

---

# Future Enhancements

Potential future improvements include:

* User Authentication and Authorization
* Role-Based Access Control
* Donation Management Module
* Email Notifications
* SMS Alerts
* QR Code Volunteer Check-In
* Social Media Integration
* Multi-Language Support
* AI Campaign Recommendations
* Geographic Impact Mapping
* Advanced Reporting and Analytics
* Mobile Application Support

---

# Learning Outcomes

This project demonstrates practical implementation of:

* Generative Artificial Intelligence
* Multimodal AI Systems
* Prompt Engineering
* Database Management
* Full Stack Development
* API Integration
* Cloud Deployment
* User Interface Design
* Data Validation Techniques
* Software Engineering Best Practices

---

# Conclusion

NayePankh Foundation is an AI-powered Multimodal NGO Campaign and Volunteer Management Platform designed to simplify campaign creation, volunteer registration, poster generation, and impact tracking.

By integrating Large Language Models, Text-to-Image AI, Database Management, and Interactive Analytics into a unified solution, the platform demonstrates how Artificial Intelligence can enhance operational efficiency and social impact initiatives.

The project showcases the practical application of Generative AI, Multimodal Systems, Full Stack Development, and Cloud Technologies to address real-world challenges faced by NGOs and community organizations.

---

# Developer

**Shraddha Upadhye**

Internship Project Submission

Domain: AI Agent Development 

Project: NayePankh Foundation – AI-Powered Multimodal NGO Campaign and Volunteer Management Platform
