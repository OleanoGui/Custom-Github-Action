# Custom GitHub Action

A customizable *GitHub Action* designed to trigger on Pull Request events and seamlessly integrate with the Slack Web-API, sending detailed logs and notifications directly to your Slack channel.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **CI/CD:** GitHub Actions
- **Integrations:** Slack Web-API

## 🤖 Features

- **Automatic triggers** on Pull Request events:
    - *opened*
    - *closed*
    - *approved*
    - *rejected*
- Real-time notifications sent to a Slack channel via the Slack Web-API
- Easy integration with your Slack workspace through a Slack App
- Customizable messages containing comprehensive Pull Request information

## 📕 Project Goals

- Deepen understanding of *GitHub Actions*
- Practice writing and configuring YAML workflows
- Gain experience with API integrations
- Improve event logging and automation skills

## ⚙️ How to Use

Integrate this action into your project by following these steps:

1. Copy both `action.yml` and `notify.js` into your project's `.github/workflows` directory.
2. Obtain a Slack API Token by creating a Slack App and installing it in your workspace. Follow the [Slack API Documentation](https://api.slack.com/start/quickstart#creating) for guidance.
3. Add your Slack API Token as a GitHub Secret in your repository:  
   Go to `Settings > Secrets > New repository secret`, name it `SLACK_API_TOKEN`, and paste your token as the value.
4. Done! Now, whenever you create a Pull Request, notifications will be sent automatically to your Slack channel. 🎉

**Tip:**  
This action is reusable! After setting it up in one project, you can call it from any other project using the following workflow snippet:

```
uses: USER_OR_ORG_NAME/REPO_NAME/.github/workflows/REUSABLE_WORKFLOW_FILE.yml@TAG_OR_BRANCH
```

For more details on reusable workflows, check out this [GitHub Blog post](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/).