# Git Commands (Sample File)
### Using Git Bash on Windows

To use these commands in Git Bash:

1. **Install Git Bash**:
   - Download and install Git for Windows from the [official Git website](https://git-scm.com/downloads).
   - During installation, choose "Git Bash" when prompted to select components.

2. **Open Git Bash**:
   - After installation, open Git Bash from the Start menu or by right-clicking in a directory and selecting "Git Bash Here".

3. **Run Git Commands**:
   - Use the Git commands as you would in any terminal.

Here is a recap of the main commands you can run in Git Bash:

### Basic Git Commands

#### **Configuration**
- `git config --global user.name "Your Name"`
- `git config --global user.email "your_email@example.com"`
- `git config --global color.ui auto`

#### **Repository Creation**
- `git init`
- `git clone <repository_url>`

#### **Basic Snapshotting**
- `git add <file>`
- `git add .`
- `git commit -m "commit message"`
- `git status`
- `git diff`
- `git diff --staged`

#### **Branching and Merging**
- `git branch`
- `git branch <branch_name>`
- `git checkout <branch_name>`
- `git checkout -b <branch_name>`
- `git merge <branch_name>`
- `git branch -d <branch_name>`

#### **Remote Repositories**
- `git remote add origin <repository_url>`
- `git remote -v`
- `git fetch <remote>`
- `git pull <remote> <branch>`
- `git push <remote> <branch>`

#### **Rewriting History**
- `git reset <file>`
- `git reset --hard <commit>`
- `git commit --amend`
- `git rebase <base_branch>`

#### **Stashing and Cleaning**
- `git stash`
- `git stash apply`
- `git stash pop`
- `git stash list`
- `git clean -fd`

#### **Inspection and Comparison**
- `git log`
- `git log --oneline`
- `git show <commit>`
- `git blame <file>`

### Example Workflow in Git Bash

1. **Initialize a Repository**:
   ```bash
   git init
   ```

2. **Clone a Repository**:
   ```bash
   git clone https://github.com/user/repository.git
   ```

3. **Make Changes and Commit**:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

4. **Create and Switch to a New Branch**:
   ```bash
   git checkout -b new-feature
   ```

5. **Make Changes, Stage, and Commit**:
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

6. **Merge the New Branch into Main Branch**:
   ```bash
   git checkout main
   git merge new-feature
   ```

7. **Push Changes to Remote**:
   ```bash
   git push origin main
   ```

8. **Handle Remote Changes**:
   ```bash
   git pull origin main
   ```

9. **Stash Changes**:
   ```bash
   git stash
   ```

10. **Apply Stash**:
    ```bash
    git stash apply
    ```
