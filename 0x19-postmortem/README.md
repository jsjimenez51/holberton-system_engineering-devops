Server Management and Web App development/deployment is handled from HQ in San Francisco.  

Deployment team was set to deploy product to servers for launch date on 2/26/19. The team was able to deploy to servers but app was not rendering in any browser. Access to product page was scheduled for 800AM PST and the delay of the product launch was until 600PM PST same day.  100% of users were affected during the Launch window and no one was able to access the product.  The root cause of the issue was found to be a firewall preventing port forwarding between servers.

The issue was detected around 700AM PST via the deployment team noticing that the product was not visible in any browser.

Assumptions made about issue:
1. Check Web Servers Configurations
2. Check Port Forwarding Configurations
3. Check Routes built into front-end
4. Check firewall usage

Actions taken:
1. Checked that web servers were up and running and that the ability to curl from servers was available. (Passed)
2. Checked Port Forwarding configurations to allow 5000:5000, 5000:5001, 5001:5001 (Passed)
3. Checked all routes were connecting via the correct ports: 5000 (Passed)
4. Checked for existing firewalls on servers and permissions granted were correct. (Failed)

Initially the deployment team was unable to detect the issue going through Actions  1-3 listed above. The incident was then escalated to the Project Manager who identified that a firewall was preventing the Port Forwarding and then tasked the deployment team to resolve the issue.

The issue was resolved by disabling the firewall as it was found unnecessary for the Web App's system design.  Utilizing the command: sudo ufw disable

Adjust Standard Operating procedures for deployments based on incident as follows:
1. Check Web Servers Configurations
2. Check Port Forwarding Configurations
3. Check Routes built into front-end
4. Check firewall usage

Making this standard practice before deployment deadlines will decrease the time to deployment and ensure that no further deadlines will be missed to due such a minor issue.  Team leads please advise your team members about this process and build into your Standard Operating Procedures.
