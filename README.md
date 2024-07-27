# Resume Matcher AI

This project is an AI-powered resume matching system that uses FastAPI, PostgreSQL, and OpenAI's language models to process resumes and match them with job descriptions.

## Prerequisites

- Docker and Docker Compose
- Python 3.12+
- pip and pip-tools

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/vaishnavghenge/llm-agent.git
   cd llm-agent
   ```

2. Create a `.env` file in the project root with the following content:
   ```
   DATABASE_URL=postgresql://user:password@db:5432/resumedb
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   Replace `your_openai_api_key_here` with your actual OpenAI API key.

3. Install pip-tools:
   ```bash
   pip install pip-tools
   ```

4. Generate `requirements.txt` from `requirements.in` (Skip if already present):
   ```bash
   pip-compile requirements.in
   ```

5. Set up pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Running the Application

To start the application and its dependencies:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## Development

### Code Formatting

This project uses Black for code formatting. The formatting is automatically run as a pre-commit hook, but you can also run it manually:

```bash
docker-compose run --rm web black .
```

### Adding New Dependencies

1. Add the new dependency to `requirements.in`.
2. Run `pip-compile requirements.in` to update `requirements.txt`.
3. Rebuild the Docker images:
   ```bash
   docker-compose build
   ```

### Database Migrations

To create a new migration:

```bash
docker-compose run --rm web alembic revision --autogenerate -m "Description of the change"
```

To apply migrations:

```bash
docker-compose run --rm web alembic upgrade head
```

## Project Structure

```
project_root/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   └── utils/
│
├── tests/
├── alembic/
├── .env
├── requirements.in
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .pre-commit-config.yaml
├── pyproject.toml
└── README.md
```

## Configuration Files

- `.pre-commit-config.yaml`: Configures pre-commit hooks, including Black for code formatting.
- `pyproject.toml`: Contains configuration for Black and other tools.
- `requirements.in`: Lists the project's direct dependencies.
- `requirements.txt`: Generated from `requirements.in`, lists all dependencies with pinned versions.

## Testing

To run tests:

```bash
docker-compose run --rm web pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.