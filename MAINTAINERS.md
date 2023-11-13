# Cherry pick changes from main to all branches: 

```
for commit in $(git log --reverse --since=yesterday --pretty=%H); do for branch in $(git branch -r | awk -F/ '/origin/{print $NF}' | grep -v '\->' | grep 'lab'); do git checkout $branch && git cherry-pick $commit && git push origin $branch ; done ; done
```