# bot_aio

## Development
---
### Kanban board
Link to the Kanban desk: https://drive.google.com/file/d/1lvN3w-KCPvQyGvFbfXvM-mOQlku4nOV4/view?usp=sharing

or this link, if you have account in Miro: https://drive.google.com/file/d/1SAXZeP9y6pCJRFgHrx-MF7KEN2ItJ8R5/view?usp=sharing

**Entry criteria for "TO DO" column:**
 - Discussion problem with team members
 - Prioritize amoung issues
 - A performer has been appointed
 - A branch has been created in the repository

**Entry criteria for "In progress" column:**
 - Prioritize amoung issues
 - Issues are estimated
 - MR has been created

**Entry criteria for "In review" column:**
 - Code fully implemented and self-reviewed
 - Pass all tests
 - Branch rebased on main
 - two reviewers assigned

**Entry criteria for "Ready to deploy" column:**
 - MR is approved
 - The documentation is updated
 - All tasks for this issue are closed

**Entry criteria for "User testing" column:**
 - Test Environment Ready
 - Customer is informed

**Entry criteria for "DONE" column:**
 - Deployment is done
 - Documentation is done
 - Testing is complete
   
### Git workflow
In this project we use GitHub flow.

**Creating issues from the defined templates**
 - We use the templates when creating
 - Try to fill in all the fields in detail and correctly

**Labelling issues**
 - Mark tasks with a label based on the size of the task (S, M, L)
 - Use a label to mark the urgency level of a task and its priority (high, medium, low)
 - Use type labels such as "Task", "Bug" etc

**Assigning issues to team members**
 - Distribute the load evenly (no more than 2-3 L-tasks per person for a sprint)
 - Assign tasks based on a person's specialization
 - The assigned executor is responsible for progress and timely status updates.

**Creating, naming, merging branches**
 - When creating a branch, name it according to its purpose
 - Make sure that name does not match the name of any existing (git branch --list)
 - Merge the branch only after you've tested the code and made sure it works

**Commit messages format**
 - Briefly and clearly describe two things: which file/directory has changed, and what changes have occurred.

**Creating a pull request for an issue using a pull request**
- 
**Illustrate your git workflow using a Gitgraph diagram.**
![Diagram](Untitled diagram _ Mermaid Chart-2025-07-06-171952.png)

**Code reviews**
 Pay attention to:
     - code clarity
     - code style
     - tests (new code should include unit/integration tests, if applicable)
     - have documentation

**Merging pull requests**
 - Minimum 2 approves
 - All tests pass (CI/CD pipeline must be successful)
 - Before merging, you must make sure that there are no conflicts with the main branch.

### Secrets management 

**Rules for secrets management:**
- Do not store secrets in the code, but use environment variables for this purpose when uploading the code somewhere.
- When developing locally, store variables in the .env file to avoid accidentally uploading them to the network.
- Never commit passwords, API keys, tokens, or other secrets directly to a repository (even a private one).

**Resolving issues**
 - Prioritization: Critical bugs and blockers first, then new features.
 - Time estimation: If a task takes longer than planned, inform the team in advance.

## Quality assurance
### Quality attribute scenarios
Description of quality scenarios: [docs/quality-assurance/quality-attribute-scenarios.md](docs/quality-assurance/quality-attribute-scenarios.md)

### Automated tests

