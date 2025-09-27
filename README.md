# web-log-manager

A web application for managing and viewing log files with a Python Flask API backend and Nuxt.js frontend.

## Prerequisites

- Node.js (for frontend)
- Python 3.x (for API)
- yarn package manager

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd web-log-manager
   ```

2. **Install frontend dependencies**
   ```bash
   yarn install
   ```

3. **Start the application**
   ```bash
   # Start both frontend and API
   yarn dev

   # Or start them separately:
   yarn dev:frontend  # Frontend only (localhost:3000)
   yarn dev:api      # API only (localhost:5000)
   ```

The API setup is fully automated - the first run will:
- Create a Python virtual environment
- Install all required Python dependencies
- Set up the database configuration
- Start the Flask API server

## Available Scripts

```bash
# Full development (frontend + API)
yarn dev

# Frontend only (Nuxt.js dev server)
yarn dev:frontend

# API only (Flask dev server)
yarn dev:api

# Production build
yarn build
yarn start

# Generate static project
yarn generate
```

## Project Structure

- `/` - Nuxt.js frontend application
- `/api/` - Python Flask API with SQLite database
- `/api/start.sh` - Automated API setup script



### Demo

![img.png](assets/demo.mp4)
