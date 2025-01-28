# Django Demo Live-Call

This project is a demo used in Backend Live-Calls to exercise Django and other Backend matters.

## Command to Fetch remote Branches

```bash
git fetch --prune && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

```powershell
git fetch --prune; git branch -vv | Select-String ': gone]' | %{ $_.ToString().Trim().Split(' ')[0] } | %{ git branch -D $_ }

```

You can automatically delete local branches that do not exist on the remote by running the following command:

This command does the following:

1. ```git fetch --prune```: Fetches the latest changes from the remote repository and prunes any remote-tracking branches that no longer exist on the remote.
2. ```git branch -vv```: Lists all local branches with additional information, including their last commit and the remote branch they are tracking.
3. ```grep ': gone]```': Filters the output to only show branches that are no longer present on the remote repository.
4. ```awk '{print $1}'```: Extracts the branch names from the filtered output.
5. ```xargs git branch -D```: Deletes the local branches that were identified in the previous step.

You can run this command manually whenever you want to clean up your local branches. Alternatively, you can set up a cron job or a scheduled task to run this command automatically at regular intervals.

Merge conflict Staging change.
Merge Conflict feature branch
