# Write-up
App Deployement using Microsoft Azure

## What Is Virtual Machine
An Azure Infrastructure as a Service (IaaS) is a type of cloud computing service that provide full access to the underlying operating system of a compute resource. These can be either Windows or Linux machines, with great availability, scalability and redundancy. These require more on-going maintenance and up-keep by cloud developers.

## What Is App Service
An Azure Platform as a Service (PaaS) is a type of cloud computing service that allow developers to focus more on their apps than the underlying infrastructure i.e Azure takes care of the infrastructure. It is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. It supports multiple languages and continuous deployment.


## Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Appropriate solution
The appropriate solution for deploying this web application is App Service.

### Why I choose App service
Comprehensive Development Environment
Azure App Service brings together everything a developer needs to create websites, mobile backends, and web APIs for any platform or device. This all-in-one platform allows for rapid development, testing, and deployment of applications without the need for managing underlying infrastructure. Key benefits include:

Infrastructure Maintenance: Azure App Service handles all the infrastructure maintenance, including updates and security patches, so developers can focus on coding rather than server management.
Scalability: It offers both automatic and manual scaling options to handle varying loads, ensuring that applications remain responsive and performant.
Security: Built-in security features protect applications from threats and vulnerabilities, with regular updates ensuring compliance with the latest standards.
Multi-Language Support
Azure App Service supports multiple programming languages, such as .NET, .NET Core, Java, Ruby, Node.js, PHP, and Python. This flexibility allows developers to use their preferred language or the language best suited for their project. In this case, the application is written in Python, which is fully supported, ensuring seamless integration and deployment.

Quick Deployment
Azure App Service allows for quick and straightforward deployment of web applications. Developers can deploy code directly from repositories or use continuous integration and deployment pipelines, reducing the time from development to production.

### Why not Virtual Machines
Avoiding Operational Overhead
Using Virtual Machines (VMs) means taking on the responsibility of managing the underlying operating system, including installing software, applying patches, and performing updates. This can be time-consuming and distracts from focusing on application development. In contrast, Azure App Service abstracts these responsibilities, providing a managed environment.

Ease of Deployment
Deploying applications on VMs often requires setting up the programming environment and managing dependencies manually. With Azure App Service, these environments are pre-configured, allowing for faster and more efficient deployment processes.

Full Management Responsibility
VMs behave like full, separate computers, which means developers are responsible for everything from security to system updates. This level of control can be advantageous in some scenarios but is generally more burdensome for routine web application deployment.

### Justification based on cost, scalability, avaliability and workflow:

Cost Efficiency
Azure App Service is generally more cost-effective compared to VMs. It offers various pricing plans, including Free and Shared (preview) plans for testing or deploying simple apps. These plans include built-in load balancers, which can significantly reduce infrastructure costs. In contrast, VMs often require additional resources and services to achieve the same level of functionality.

Scalability
Azure App Service provides robust scaling options:

Vertical Scaling: Automatically adjusts resources like vCPUs or RAM by changing the pricing tier.
Horizontal Scaling: Adjusts the number of VM instances running the app, based on metrics such as CPU usage, memory consumption, or HTTP queue length.
These scaling options ensure that the application can handle increased loads without manual intervention, maintaining performance and reliability.

Availability
Azure App Service guarantees high availability with its global datacenter infrastructure. Applications can be hosted anywhere within Microsoft's extensive network of data centers, benefiting from redundancy and failover capabilities. The App Service SLA (Service Level Agreement) promises high availability, ensuring that applications remain accessible even during maintenance or unexpected downtimes.

Streamlined Workflow
Azure App Service supports automated deployments from GitHub, Azure DevOps, or any Git repository. Developers can leverage GitHub Actions for Azure web apps to create workflows that automate the build, test, package, release, and deploy processes. This integration enhances productivity and ensures that the latest code changes are consistently and reliably deployed. 

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

- Azure app service has a hardware limitations. Also is not an appropriate solution for apps which have scope to expand for future. Instead, VMs are preferred. If this app grows to a larger scale, when we have vast increase in the number of users or when more features are added to the app, I would choose a Virtual Machine.

Hardware Limitations and Future Scalability Concerns
Azure App Service, while highly efficient for small to medium-scale applications, does have inherent hardware limitations. These limitations can impact applications that anticipate significant growth in user base or functionality. Here are some key considerations:

Resource Cap: Azure App Service plans come with predefined resource limits (CPU, memory, storage) which may not be sufficient for applications that experience a vast increase in users or require more intensive processing power.
Scaling Restrictions: Although App Service supports scaling, it may not handle extremely high traffic or complex scaling scenarios as efficiently as VMs can with Virtual Machine Scale Sets (VMSS).
Preferred Solution for Large-Scale Applications
When an application grows to a larger scale, Virtual Machines become the preferred solution due to their flexibility and control. Here are specific scenarios where VMs are advantageous:

Advanced Scaling and Traffic Management: VMs, especially when used with VMSS, offer advanced auto-scaling and traffic management features. This allows applications to handle significant increases in load by automatically adding or removing VM instances based on demand, ensuring optimal performance and cost-efficiency.
Custom Environments: If the application needs to be implemented using a programming language or technology stack not supported by Azure App Service, VMs offer the flexibility to create custom environments. This can be critical for specialized applications or those that leverage newer or less common technologies.
Enhanced Control and Customization
Using Azure App Service limits access to the underlying infrastructure, which may not be suitable for applications requiring extensive customization. Here are the detailed advantages of VMs in this context:

Full OS Access: With VMs, developers have full control over the operating system, enabling them to install custom software, apply specific configurations, and optimize the environment for their application’s needs.
Advanced Configuration and Tuning: For performance-critical applications, VMs allow for advanced system tuning and configuration that are not possible with Azure App Service. This includes custom networking setups, specialized security configurations, and the use of specific hardware features.
