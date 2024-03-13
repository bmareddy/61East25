Data Platforms such as Fivetran or Matillion are regarded as essential in Modern Data Stack and have quickly replaced legacy in house solutions or previous generation enterprise solutions. However, it is important to evaluate and understand how they fit in your organizations needs, architecture and resources. 

### Fivetran / Matillion / (Insert any data platform vendor)

**Pros:**

1. **No Code:** They offer a user-friendly interface, allowing users to set up and manage workflows with minimal or no coding. This can significantly reduce the barrier to stand up
a platform and unlock business value.
2. **Connectors:** Almost all of these vendor platforms come with wide range of pre-built connectors to various data sources and destinations. It is very likely there will not be any need for custom development, and onboarding new data sources is just a task instead of a project.
3. **Managed Service:** As managed solutions, they handle infrastructure, maintenance, and updates, reducing the burden on your SRE / DevOps team and lowering operational overhead.
4. **Scalability:** These tools are designed to automatically scale to handle large volumes of data and complex transformations, ensuring performance as your data needs grow.

**Cons:**

1. **Cost:** These services can be expensive, especially at scale. Pricing often depends on the volume of data processed, the number of connectors, and the level of service, which might not be cost-effective for smaller organizations or projects.
2. **Support:** While basic service tends to be good, when there are hard problems or mission critical issues, your are dependent on your middle management and third party vendor to collaborate and come to resolution. It is much harder to achieve this in practice
3. **Reliability:** The Modern Data Stack space is extremely competitive and is constantly evolving, maturing and consolidating. If the vendor goes out of business or goes through M&A, your organization could be negative impacted, forcing your team to spend valuable resources on migration projects
4. **Complexity:** While they offer broad connector options, there may be limitations in customization or support for edge cases that may be a common case in your organization.

### Writing Code In-House

**Pros:**

1. **Architecture Conformity:** Building in-house solutions allows the solution to follow same architecture and design principles as rest of the code base which provides long term value.
2. **Customization:** Building your own data ingestion tools allows for complete customization to meet your exact requirements and integrate tightly with your existing systems.
3. **Control:** Full control over the data ingestion process, including the ability to modify or optimize the system as your needs evolve.
4. **Cost Considerations:** For some organizations, particularly those with specific requirements or with available in-house expertise, developing and maintaining a custom solution might be more cost-effective in the long run.

**Cons:**

1. **Team with Right Skills:** Requires a team of skilled engineers with a strong tech lead who understands both the technical and operational aspects of data integration for initial development.
2. **Org Culture:** As with any investments, there has to be a champion that supports the investment and advocates for this option which is subject to internal politics
4. **Time & Execution:** Developing a custom solution can take significant time, typically 2-6 months delaying the ability to derive value from your data. And even the best plans and designs are only as good as their implementation. So getting the execution right is critical to the success

Ultimately, the choice between using vendor solutions or developing an in-house solution depends on your organization's specific needs, including the complexity of your data ecosystem, the skills of your team, your budget, and org culture.