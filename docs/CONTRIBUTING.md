
## Git workflow
All project code you can find in our Github, however the main backlog is on our [Gitlab repository](https://gitlab.pg.innopolis.university/dashboard/issues?sort=created_date&state=opened&assignee_username[]=d.evdokimova).<br>
Our team has several rules of operation:

#### Creating issues from the defined templates
 - We use the templates when creating
 - Try to fill in all the fields in detail and correctly

**Labelling issues**
 - Mark tasks with a label based on the size of the task _(S, M, L)_
 - Use a label to mark the urgency level of a task and its priority _(high, medium, low)_
 - Use type labels such as "Task", "Bug" etc

**Assigning issues to team members**
 - Distribute the load evenly _(no more than 2-3 L-tasks per person for a sprint)_
 - Assign tasks based on a person's specialization
 - The assigned executor is responsible for progress and timely status updates.

**Creating, naming, merging branches**
 - When creating a branch, name it according to its purpose
 - Make sure that name does not match the name of any existing _(git branch --list)_
 - Merge the branch only after you've tested the code and made sure it works

**Commit messages format**
 - Briefly and clearly describe two things: which file/directory has changed, and what changes have occurred.

### Gitgraph diagram
![GitGraph diagram](structure/Gitgraph_workflow_diagram.png)

**Code reviews** ( Pay attention to: )
 - Code clarity
 - Code style_
 - Tests _(new code should include unit/integration tests, if applicable)
 - Documentation

**Merging pull requests**
 - Minimum 2 approves
 - All tests pass _(CI/CD pipeline must be successful)_
 - Before merging, you must make sure that there are no conflicts with the main branch.

### Secrets management 
**Rules for secrets management:**
- Do not store secrets in the code, but use environment variables for this purpose when uploading the code somewhere.
- When developing locally, store variables in the .env file to avoid accidentally uploading them to the network.
- Never commit passwords, API keys, tokens, or other secrets directly to a repository _(even a private one)_.

**Resolving issues** 
 - **Prioritization:** Critical bugs and blockers first, then new features.
 - **Time estimation:** If a task takes longer than planned, inform the team in advance.
   
# Development
[**Link to the Kanban board**](https://drive.google.com/file/d/1lvN3w-KCPvQyGvFbfXvM-mOQlku4nOV4/view?usp=sharing) or this [**link**](https://drive.google.com/file/d/1SAXZeP9y6pCJRFgHrx-MF7KEN2ItJ8R5/view?usp=sharing), if you have account in Miro 
