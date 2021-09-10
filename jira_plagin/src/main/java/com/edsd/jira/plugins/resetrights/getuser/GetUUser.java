package com.edsd.jira.plugins.resetrights.getuser;

//import com.atlassian.jira.bc.JiraServiceContextImpl;
//import com.atlassian.jira.bc.user.search.UserSearchParams;
//import com.atlassian.jira.bc.user.search.UserSearchService;
import com.atlassian.jira.component.ComponentAccessor;
import com.atlassian.jira.user.ApplicationUser;

public class GetUUser {
    UserSearchParams.Builder paramBuilder = UserSearchParams.builder()
            .allowEmptyQuery(true)
            .includeActive(true)
            .includeInactive(true)

    ApplicationUser loggedInUser = ComponentAccessor.getJiraAuthenticationContext().getLoggedInUser()
    JiraServiceContextImpl jiraServiceContext = new JiraServiceContextImpl(loggedInUser)

    Collection<ApplicationUser> users = ComponentAccessor.getComponent(UserSearchService).findUsers(jiraServiceContext, "", paramBuilder.build())
}


