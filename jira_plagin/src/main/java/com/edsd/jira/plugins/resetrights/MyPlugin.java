package com.edsd.jira.plugins.resetrights;

import com.atlassian.jira.project.Project;
import com.atlassian.jira.web.action.JiraWebActionSupport;
import com.atlassian.jira.user.util.UserManager;

public class MyPlugin extends JiraWebActionSupport {
    private Project project;

    @Override
    public String execute() throws Exception {

        project = getSelectedProjectObject();
        request.setAttribute("com.atlassian.jira.projectconfig.util.ServletRequestProjectConfigRequestCache:project", project);

        return super.execute();
    }
    public Project getProject() {
        return project;
    }
}
