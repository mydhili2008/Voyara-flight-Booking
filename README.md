# Voyara — Cinematic Flight Booking Demo

A responsive, cinematic flight-booking website concept built with **HTML, CSS, JavaScript and Python Flask**. Includes layered parallax, scroll reveals, animated aircraft, sample search results, and a demo booking flow.

> **Important:** Voyara is a front-end/back-end portfolio prototype. All flight schedules and prices are fictional sample data. It does not connect to airline/GDS inventory, issue tickets, store bookings, or process real payments. A demo confirmation is not a ticket.

## Features
- Full-screen cinematic hero with video background and image fallback
- Responsive layout for mobile, tablet and desktop
- Scroll-triggered reveal animations and layered parallax
- Animated airplane path and interactive origin/destination swap
- Search form and sample flight results
- Demo passenger form and confirmation screen
- Flask routes, Jinja templates, accessible labels, reduced-motion support
- No API keys or paid services required

## Requirements
- Python 3.10+
- pip

## Run locally

### Windows (PowerShell)
```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python app.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Project structure
```text
voyara-flight-booking/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   ├── book.html
│   ├── confirmation.html
│   └── 404.html
└── static/
    ├── css/styles.css
    ├── js/main.js
    └── images/README.md
```

## GitHub upload
1. Extract the ZIP.
2. Create a repository named `voyara-flight-booking`.
3. Upload the **contents** of the extracted folder (not the ZIP itself).
4. Commit the files to the `main` branch.
5. Add a short repository description such as “Cinematic Flask flight-booking demo”.

## Deployment notes
For a public deployment, use a production WSGI server such as Gunicorn and configure a strong `SECRET_KEY` environment variable. Do not deploy Flask's development server or `debug=True` publicly. A static host such as GitHub Pages cannot run Flask/Python; use a Python-capable host.

## Production integration still needed
- Real flight search provider/API and its licensing
- Server-side validation, persistent database and booking lifecycle
- Authentication and secure passenger-data handling
- Real payment provider integration with PCI-compliant checkout
- Tests, rate limiting, logging, privacy policy and production security settings
