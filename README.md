## Penta_Core

## Who Did What

| Member           | GitHub Username           | File             |
| ---------------- | ------------------------- | ---------------- |
| Pyae Sone        | 6805140013-hub            | test_teardown.py |
| Zaw Thant Khaing | ZawThantKhaing-6805140017 | test_withdraw.py |
| Zaw Win Aung     | ZawWinAung-6805140022     | test_deposit.py  |
| Shu Maung        | ShuMaung-6805140021 ,     | test_shared.py   |
                     shu-maung-6805140021
| Ye Min Thant     | 6805140015-collab         | conftest.py      |

## Our Merge Conflict

# 1. Conflict Markers Encountered

While working on the ## Who Did What section of our documentation, our team encountered the following merge conflict markers: Plaintext<<<<<<< HEAD (Current Change)
| Member | GitHub Username | File |
|---|---|---|
| Pyae Sone | 6805140013-hub | test_teardown.py |
=======
| Member | GitHub Username | File |
|---|---|---|
| Zaw Thant Khaing | ZawThantKhaing-6805140017 | test_withdraw.py |

> > > > > > > b7236e44f39fe717c689ae6d37cdece45f7444bc (Incoming Change)

# 2. Lines Kept in the Final Version

| Since both team members were adding valid contributions to the table, we decided to accept both changes. We cleaned up the duplicate table headers and kept both data rows. The final resolved lines are:Markdown | Member                    | GitHub Username  | File |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ---------------- | ---- |
| Pyae Sone                                                                                                                                                                                                         | 6805140013-hub            | test_teardown.py |
| Zaw Thant Khaing                                                                                                                                                                                                  | ZawThantKhaing-6805140017 | test_withdraw.py |

# 3. Why Git Could Not Resolve

This AutomaticallyGit could not resolve this conflict automatically because two different team members attempted to add their respective table rows on the exact same lines (directly under the ## Who Did What heading) in parallel. When Git attempts to merge these changes, it sees two competing edits for the same exact line numbers. Because Git does not understand the context of the Markdown table, it cannot safely determine whether to overwrite one change with the other, or in what order to combine them. Instead, it stops the merge process and injects conflict markers so that a human developer can manually review and structure the final table.

## Git Contribution Summary

Output of `git shortlog -sn`:
```text
     8  Shu Maung
     7  Pyae Sone
     3  Ye Min Thant
     4  Zaw Thant Khaing
     3  ZawWinAung
```
## Reflection Questions

# Why was your push rejected, and how did you fix it?

The push was rejected because another teammate uploaded changes to GitHub first, meaning the local repository was out of date. It was fixed by running git pull to download and merge their latest changes, followed by running git push again.

# Why could Git not resolve the README conflict automatically?

Git could not resolve the conflict automatically because multiple team members made changes to the exact same part of the README.md file. Git cannot determine on its own which version should be kept in the final file, so it requires manual human intervention to choose the correct lines.

# What is the difference between committing and pushing?

Committing saves a snapshot of your changes only to the local repository on your own computer. Pushing uploads those saved commits to the shared remote repository on GitHub so that your teammates can access your work.

# How do fixtures reduce duplicated setup code in tests?

Fixtures allow you to write a setup step (like creating a starting BankAccount with a specific balance) exactly once. Multiple tests can then automatically reuse this setup by referencing the fixture name, eliminating the need to rewrite the object creation steps in every single test function.
