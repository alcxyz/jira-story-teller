# jira-story-teller
Python automation to create Jira stories and sub-tasks using the Jira REST API.

The script reads story summaries or task descriptions from an external text file, stories.txt, and creates Jira stories or sub-tasks for each of them under the specified project, epic, or parent story.

The script prompts the user for their Jira instance URL, email, project key, and epic or parent key, ensuring secure and customizable input. To customize it further according to your own Jira configuration, you should adjust the field identifier "customfield_10118" in the script to match your Epic Issue customfield ID.

The script expects a valid API key to be placed inside a file named api-key.txt. This script is intended to save time and streamline the process of creating multiple Jira stories and sub-tasks in a project, making it an efficient and user-friendly solution for project management. Please make sure to adjust settings according to your specific Jira instance configuration for optimal results.

## To obtain the custom field for Epic Issues in Jira, follow the steps below:
1. Log into your Jira instance and navigate to any issue page.
2. Locate the "Epic Link" field.
3. Right-click on the "Epic Link" field and choose "Inspect" from the context menu. This will open up your browser's developer tools and highlight the code for that field.
4. In the highlighted code, look for something like id="customfield_XXXXX". The XXXXX is the ID of the custom field for Epic Issues. Remember to replace "customfield_10118" in the script with your specific Epic Link custom field ID for proper functioning.

Please note that the exact instructions may vary slightly based on the browser you're using. These steps are generally applicable to Chrome, Firefox, and Safari.
