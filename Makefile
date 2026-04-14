.PHONY: run test cov migrate db-upgrade db-downgrade lint format docker-up docker-down clean

# ── Desenvolvimento ──
run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# ── Testes ──
test:
	poetry run pytest -v

cov:
	poetry run pytest --cov=app --cov-report=term-missing -v

# ── Banco de Dados ──
migrate:
	poetry run alembic revision --autogenerate -m "$(msg)"

db-upgrade:
	poetry run alembic upgrade head

db-downgrade:
	poetry run alembic downgrade -1

# ── Qualidade de Código ──
lint:
	poetry run ruff check app/ tests/

lint-fix:
	poetry run ruff check --fix app/ tests/

format:
	poetry run ruff format app/ tests/

# ── Docker ──
docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f

# ── Limpeza ──
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache htmlcov .coverage
