# MyFitnessJourney

A completely free and open source fitness tracking app. Document your fitness journey, visualize progress, and achieve your goals without any cost or limitations.

## Features

- Robust REST API architecture - Focusing on security and scalability.
- Modern Vue 3 Frontend – A fast, reactive user interface leveraging the Composition API.
- PrimeVue UI Suite – Premium, accessible component library integrated.
- Utility-First Styling – Fully responsive and highly customizable design powered by Tailwind CSS.
- Authentication – Token-based authentication and JWT via Django for secure user access.
- State Management – Secure user login and registration powered by Pinia.
- API Documentation – Automatically generated Swagger/Redoc documentation for easy endpoint testing.

## Tech Stack

- Backend: Django & Django REST Framework (DRF)
- Frontend: Vue.js 3 (Composition API), Vite
- Styling: Tailwind CSS, PrimeVue
- Database: SQLite3
- CI/CD: GitHub Actions (Not Implemented Yet).
- Hosting: At the moment only local development.

## Quick Start

### Prerequisites

- Python 3.14
- Node.js (v20+) & npm

### Run on Local

Clone the repository and install dependencies:

```shell
git clone https://github.com/peek4bUh/my-fitness-journey
```

#### Backend

1. Create a virtual environment:

```shell
cd api & python -m venv venv
source venv/bin/activate
```

2. Install Dependencies:

```shell
pip install -r requirements.txt 
```

3. Run Django migrations:

```shell
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:

```shell
python manage.py runserver
```

The REST API will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

#### Frontend

1. Install Dependencies:

```shell
cd ../vue-project && npm install
```

2. Start the development server:

```shell
python manage.py runserver
```

The app will be available at [http://localhost:5173/](http://localhost:5173/).

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)