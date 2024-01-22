#!/bin/bash

# Prompt for the new project name
read -p "Enter the new project name: " project_name

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install GitHub CLI
if ! command -v gh &> /dev/null
then
    echo "Installing GitHub CLI..."
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
    sudo apt update
    sudo apt install gh
fi

# Clone specific files from the Git repository
git init $project_name
cd $project_name
git sparse-checkout init --cone
git remote add -f origin <URL_of_your_template_repository>
git sparse-checkout set config.py dataloading.py pyproject.toml pyproject.lock

# Create new Poetry project using the existing pyproject.toml
mv pyproject.toml pyproject_backup.toml
poetry new $project_name --name $project_name

# Replace project name in pyproject.toml
python3 -c "import toml; \
            data = toml.load('pyproject_backup.toml'); \
            data['tool']['poetry']['name'] = '$project_name'; \
            toml.dump(data, open('pyproject.toml', 'w'))"

# Update Poetry dependencies
poetry update

# Initialize new Git repository and commit
git add .
git commit -m "Initial commit for $project_name"

# Push to a new GitHub repository
gh auth login
gh repo create $project_name --public --source=.
git push -u origin master
