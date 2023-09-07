import json
import requests

class JiraAuth:
    def __init__(self, email, api_token):
        self.email = email
        self.api_token = api_token

def create_jira_issue(auth, jira_url, project_key, issue_type, parent_key, summary, description, labels):
    adf_description = {
        "version": 1,
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": description
                    }
                ]
            }
        ]
    }

    issue = {
        "fields": {
            "project": {"key": project_key},
            "issuetype": {"name": issue_type},
            "summary": summary,
            "description": adf_description,
            "labels": labels,
        }
    }

    if parent_key:
        if issue_type == "Story":
            issue["fields"]["customfield_10118"] = parent_key
        elif issue_type == "Sub-task":
            issue["fields"]["parent"] = {"key": parent_key}
            issue["fields"]["issuetype"] = {"name": "Sub-task"}

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{jira_url}/rest/api/3/issue",
        auth=(auth.email, auth.api_token),
        headers=headers,
        data=json.dumps(issue),
    )

    if response.status_code != 201:
        print(response.text)  # Uncomment this line to print error messages
        raise Exception(f"Failed to create issue, status code: {response.status_code}")

    created_issue = response.json()
    return created_issue["key"]

def main():
    jira_url = input("Enter your Jira domain: ").strip()
    email = input("Enter your email: ").strip()

    with open('api-key', 'r') as api_key_file:
        api_token = api_key_file.readline().strip()

    auth = JiraAuth(email, api_token)
    project_key = input("Enter your project key: ").strip()

    issue_types = ["Story", "Sub-task"]
    issue_type = input("Choose the issue type (Story or Sub-task): ").strip()
    if issue_type not in issue_types:
        print("Invalid issue type. Exiting.")
        return

    parent_key = input(f"Enter the {(lambda x: 'epic' if x == 'Story' else 'story')(issue_type)} key: ").strip()
    label = input("Enter a label for the issue: ").strip()

    with open('stories.txt', 'r') as f:
        summary_list = [line.strip() for line in f.readlines()]

    for summary in summary_list:
        description = f"Address the following task: {summary}"
        labels = [label]
        created_issue_id = create_jira_issue(auth, jira_url, project_key, issue_type, parent_key, summary, description, labels)
        print(f"Created issue with ID {created_issue_id}")

if __name__ == "__main__":
    main()
