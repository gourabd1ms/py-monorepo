# py-monorepo

A monorepo containing two independent Python projects, each analyzed
**individually** by SonarQube Cloud (org `gourabd1ms`, host `https://sonarqube.us`).

```
projects/
├── service_a/   -> Sonar project  gourabd1ms_py-monorepo_service_a
└── service_b/   -> Sonar project  gourabd1ms_py-monorepo_service_b
```

## How per-project analysis works

Each project directory is self-contained:

* its own `pyproject.toml`, `src/`, and `tests/`
* its own `sonar-project.properties` with a **distinct `sonar.projectKey`**
* its own `coverage.xml` (pytest + coverage), referenced by
  `sonar.python.coverage.reportPaths`

The CI workflow `.github/workflows/sonar.yml` runs a **matrix job per project**.
Each job scans only its subdirectory via
`SonarSource/sonarqube-scan-action` with `projectBaseDir: projects/<name>`,
so issues, coverage and the quality gate are scoped to that one project.

## One-time SonarQube Cloud setup for this repo

1. **Add the CI secret**: repo *Settings → Secrets and variables → Actions →*
   `SONAR_TOKEN` = a SonarQube Cloud token for org `gourabd1ms`.
2. **Bind the repo in monorepo mode**: in SonarQube Cloud, *Import / Analyze*
   this GitHub repo and enable **"This is a monorepo"**, then map each Sonar
   project (`..._service_a`, `..._service_b`) to it. This is what lets one
   GitHub repo carry multiple Sonar projects and enables **PR decoration**
   per project.

The projects themselves are auto-created on first run by the "Ensure Sonar
project exists" step, but the monorepo binding in step 2 must be done in the UI.

## Run locally

```bash
cd projects/service_a
pip install -e . pytest coverage
coverage run --source=src -m pytest && coverage report
```
