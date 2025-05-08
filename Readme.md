# Django Demo Live-Call

This project is a demo used in Backend Live-Calls to exercise Django and other Backend matters.

---

## Prerequisites

- **GIT**: to download the Repository
- **Python** if you prefer to start on your local machine: version that is supported by the Django Version set in [requirements.txt](./requirements.txt)
- **Docker** if you prefer to start inside of container

---

## Quickstart

### Download and setup Environments

```shell
# Clone Repository
git clone https://github.com/mihaiandreineacsu/django-example.git
# Navigate to project
cd django-example

# Create a .env file from template.env file
cp template.env .env  # for bash (Linux/MacOS)
Copy-Item -Path template.env -Destination .env  # for powershell (Windows)
# Replace the default values from template.env in .env with your own
```

### Starting the project on your local machine

```bash
# Create a local python environment
python -m venv venv

# Activate python virtual environment
source env/bin/activate  # for bash (Linux/MacOS)
.\venv\Scripts\Activate  # for powershell (Windows)

# Install requirements
pip install -r requirements.txt

# Create Database and migration files
python manage.py makemigrations

# Create Tables in Database
python manage.py migrate

# Start development server
python manage.py runserver
```

### Staring the project using docker

```bash
# Build Docker Image
docker build -t django_example .

# Start the container in bash (Linux/MacOS)
docker run -it --rm \
    --name django_example \
    --env-file .env \
    -p 8000:8000 \
    -v $(pwd):/app \
    django_example

# Start the container in powershell (Windows)
docker run -it --rm `
    --name django_example `
    --env-file .env `
    -p 8000:8000 `
    -v ${PWD}:/app `
    django_example
```

Open the application on [localhost:8000](http://localhost:8000)

---

## Development

### Vscode Extensions (Optional)

- **Mogami**: Used to check Requirements latest version. <https://marketplace.visualstudio.com/items/?itemName=ninoseki.vscode-mogami>
- **Code Spell Checker**: Used to correct languages. <https://marketplace.visualstudio.com/items/?itemName=streetsidesoftware.code-spell-checker>
- **markdownlint**: Visualization of MarkDown files and linting. <https://marketplace.visualstudio.com/items/?itemName=DavidAnson.vscode-markdownlint>

### Command to Fetch remote Branches (Optional)

```bash
git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

```powershell
git fetch --prune; git branch -vv | Select-String ': gone]' | %{ $_.ToString().Trim().Split(' ')[0] } | %{ git branch -D $_ }

```

You can automatically delete local branches that do not exist on the remote by running the following command:

This command does the following:

1. ```git fetch --prune```: Fetches the latest changes from the remote repository and prunes any remote-tracking branches that no longer exist on the remote.
1. ```git branch -vv```: Lists all local branches with additional information, including their last commit and the remote branch they are tracking.
1. ```grep ': gone]```': Filters the output to only show branches that are no longer present on the remote repository.
1. ```awk '{print $1}'```: Extracts the branch names from the filtered output.
1. ```xargs git branch -D```: Deletes the local branches that were identified in the previous step.

You can run this command manually whenever you want to clean up your local branches. Alternatively, you can set up a cron job or a scheduled task to run this command automatically at regular intervals.
