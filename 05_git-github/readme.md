# Git Commands Cheat Sheet for Developers

## What is Git?

Git is a distributed version control system used to track changes in source code during software development. It allows multiple developers to collaborate efficiently, maintain code history, and manage project versions.

---

# 1. Repository Commands

## git init

Creates a new Git repository in the current directory.

```bash
git init
```

**Purpose:** Starts version control for a project.

---

## git clone

Copies an existing remote repository to your local machine.

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/user/project.git
```

**Purpose:** Downloads an existing project.

---

# 2. Configuration Commands

## git config

Configures Git settings.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

View configuration:

```bash
git config --list
```

**Purpose:** Sets user identity and Git preferences.

---

# 3. Status and History Commands

## git status

Shows the current status of files.

```bash
git status
```

**Purpose:** Displays modified, staged, and untracked files.

---

## git log

Shows commit history.

```bash
git log
```

**Purpose:** Displays all commits with detailed information.

---

## git log --oneline

Shows compact commit history.

```bash
git log --oneline
```

**Purpose:** Displays commits in a short format.

---

## git show

Displays detailed information about a commit.

```bash
git show
```

**Purpose:** Shows commit changes and metadata.

---

## git diff

Shows changes between versions.

```bash
git diff
```

**Purpose:** Compares modifications before committing.

---

# 4. Staging Commands

## git add

Adds files to the staging area.

```bash
git add file.txt
git add .
```

**Purpose:** Prepares files for commit.

---

## git restore --staged

Removes files from staging.

```bash
git restore --staged file.txt
```

**Purpose:** Unstages files while keeping changes.

---

# 5. Commit Commands

## git commit

Creates a commit.

```bash
git commit -m "Added login feature"
```

**Purpose:** Saves a snapshot of staged changes.

---

## git commit --amend

Modifies the latest commit.

```bash
git commit --amend
```

**Purpose:** Updates the last commit message or content.

---

# 6. Branch Commands

## git branch

Lists all branches.

```bash
git branch
```

**Purpose:** Displays available branches.

---

## git branch <branch-name>

Creates a new branch.

```bash
git branch feature-auth
```

**Purpose:** Creates a separate development line.

---

## git branch -d

Deletes a branch.

```bash
git branch -d feature-auth
```

**Purpose:** Removes a merged branch.

---

## git branch -D

Force deletes a branch.

```bash
git branch -D feature-auth
```

**Purpose:** Deletes a branch regardless of merge status.

---

## git branch -m

Renames a branch.

```bash
git branch -m new-name
```

**Purpose:** Changes branch name.

---

# 7. Branch Switching Commands

## git checkout

Switches branches.

```bash
git checkout feature-auth
```

**Purpose:** Moves to another branch.

---

## git checkout -b

Creates and switches to a new branch.

```bash
git checkout -b feature-auth
```

**Purpose:** Saves time by creating and switching in one command.

---

## git switch

Modern way to switch branches.

```bash
git switch feature-auth
```

**Purpose:** Changes current branch.

---

## git switch -c

Creates and switches to a branch.

```bash
git switch -c feature-auth
```

**Purpose:** Creates and moves to a new branch.

---

# 8. Merge Commands

## git merge

Combines branches.

```bash
git merge feature-auth
```

**Purpose:** Integrates branch changes.

---

## git merge --abort

Cancels a merge.

```bash
git merge --abort
```

**Purpose:** Returns repository to pre-merge state.

---

# 9. Remote Repository Commands

## git remote add

Adds a remote repository.

```bash
git remote add origin <repository-url>
```

**Purpose:** Connects local repository to GitHub.

---

## git remote -v

Displays remotes.

```bash
git remote -v
```

**Purpose:** Shows configured remote URLs.

---

## git remote remove

Removes a remote repository.

```bash
git remote remove origin
```

**Purpose:** Deletes remote connection.

---

# 10. Push Commands

## git push

Uploads commits.

```bash
git push
```

**Purpose:** Sends local commits to remote repository.

---

## git push -u origin main

Pushes and sets upstream branch.

```bash
git push -u origin main
```

**Purpose:** Links local and remote branches.

---

## git push --force

Force pushes commits.

```bash
git push --force
```

**Purpose:** Overwrites remote history.

⚠️ Use carefully.

---

# 11. Fetch and Pull Commands

## git fetch

Downloads remote changes.

```bash
git fetch
```

**Purpose:** Retrieves updates without merging.

---

## git fetch --all

Fetches all remotes.

```bash
git fetch --all
```

**Purpose:** Downloads updates from all remotes.

---

## git pull

Downloads and merges changes.

```bash
git pull
```

**Purpose:** Updates local branch.

---

## git pull --rebase

Pulls changes using rebase.

```bash
git pull --rebase
```

**Purpose:** Maintains linear commit history.

---

# 12. Rebase Commands

## git rebase

Moves commits onto a new base.

```bash
git rebase main
```

**Purpose:** Keeps commit history clean.

---

## git rebase -i

Interactive rebase.

```bash
git rebase -i HEAD~5
```

**Purpose:** Edit, reorder, squash, or delete commits.

---

## git rebase --continue

Continues rebase process.

```bash
git rebase --continue
```

**Purpose:** Resumes after conflict resolution.

---

## git rebase --abort

Cancels rebase.

```bash
git rebase --abort
```

**Purpose:** Restores previous repository state.

---

# 13. Reset Commands

## git reset --soft

Removes commit but keeps changes staged.

```bash
git reset --soft HEAD~1
```

**Purpose:** Undo commit safely.

---

## git reset --mixed

Removes commit and unstages changes.

```bash
git reset --mixed HEAD~1
```

**Purpose:** Undo commit and staging.

---

## git reset --hard

Deletes commit and changes.

```bash
git reset --hard HEAD~1
```

**Purpose:** Completely discards work.

⚠️ Dangerous command.

---

# 14. Revert Command

## git revert

Creates a new commit that reverses previous changes.

```bash
git revert <commit-id>
```

**Purpose:** Safely undo commits.

---

# 15. Stash Commands

## git stash

Temporarily saves changes.

```bash
git stash
```

**Purpose:** Store work without committing.

---

## git stash list

Lists stashes.

```bash
git stash list
```

**Purpose:** View saved work.

---

## git stash apply

Applies stash.

```bash
git stash apply
```

**Purpose:** Restore changes without removing stash.

---

## git stash pop

Applies and removes stash.

```bash
git stash pop
```

**Purpose:** Restore and delete stash entry.

---

## git stash clear

Deletes all stashes.

```bash
git stash clear
```

**Purpose:** Removes all temporary saves.

---

# 16. Tag Commands

## git tag

Creates a tag.

```bash
git tag v1.0
```

**Purpose:** Marks releases and milestones.

---

## git tag -a

Creates annotated tag.

```bash
git tag -a v1.0 -m "Release Version 1.0"
```

**Purpose:** Stores extra metadata.

---

## git push --tags

Pushes tags.

```bash
git push --tags
```

**Purpose:** Uploads tags to remote repository.

---

# 17. Cherry-Pick Command

## git cherry-pick

Copies a commit from another branch.

```bash
git cherry-pick <commit-id>
```

**Purpose:** Applies a specific commit.

---

# 18. Clean Commands

## git clean -f

Deletes untracked files.

```bash
git clean -f
```

**Purpose:** Removes unnecessary files.

---

## git clean -fd

Deletes untracked files and folders.

```bash
git clean -fd
```

**Purpose:** Cleans repository workspace.

---

## git clean -n

Preview cleanup.

```bash
git clean -n
```

**Purpose:** Shows what would be deleted.

---

# 19. Inspection Commands

## git blame

Shows who modified each line.

```bash
git blame file.txt
```

**Purpose:** Tracks line ownership.

---

## git bisect

Finds buggy commits.

```bash
git bisect start
```

**Purpose:** Uses binary search to locate issues.

---

# Common Git Interview Questions

## Difference Between git fetch and git pull

| git fetch          | git pull                     |
| ------------------ | ---------------------------- |
| Downloads changes  | Downloads and merges changes |
| Safe operation     | Modifies local branch        |
| No automatic merge | Automatic merge              |

---

## Difference Between git merge and git rebase

| git merge            | git rebase       |
| -------------------- | ---------------- |
| Preserves history    | Rewrites history |
| Creates merge commit | Linear history   |
| Easier for teams     | Cleaner history  |

---

## Difference Between git reset and git revert

| git reset                | git revert              |
| ------------------------ | ----------------------- |
| Removes commits          | Creates undo commit     |
| Rewrites history         | Preserves history       |
| Risky on shared branches | Safe on shared branches |

---

## Difference Between stash apply and stash pop

| stash apply       | stash pop           |
| ----------------- | ------------------- |
| Restores stash    | Restores stash      |
| Keeps stash entry | Deletes stash entry |

---

# Daily Developer Workflow

```bash
git clone <repo-url>

git switch -c feature-login

git add .

git commit -m "Added login page"

git push origin feature-login

git pull origin main

git merge main

git push origin feature-login
```

---

# Top 10 Most Used Git Commands

```bash
git clone
git status
git add .
git commit -m
git push
git pull
git branch
git switch
git merge
git stash
```

Master these commands first before learning advanced Git concepts.
