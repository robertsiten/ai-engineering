
ESTIMATION_EXAMPLES: list[dict] = [
    {
        "meeting_summary": (
            "A public sector organization needs a web-based case management system to "
            "replace an outdated desktop application. The platform must support case "
            "registration, document uploads, configurable approval workflows, role-based "
            "access for analysts, supervisors, and administrators, and automatic generation "
            "of unique case reference numbers. Users need to search and filter cases by "
            "status, department, date, and assigned employee. The system must maintain "
            "a complete audit trail of every action and generate PDF reports. The existing "
            "data is stored in SQL Server and must be migrated to the new platform. "
            "The proposed technology stack is ASP.NET Core for the REST API and React "
            "for the frontend. Deployment will be performed on internal infrastructure "
            "using Docker containers."
        ),
        "estimation": """\
## Enterprise Case Management and Approval System

### Task Breakdown

| Task | Hours | Cost (EUR) |
|------|------:|------------|
| Requirements analysis and workflow mapping | 20 | 1,250 |
| Solution architecture and technical design | 16 | 1,000 |
| SQL Server schema design and data migration | 28 | 1,750 |
| Authentication and role-based authorization | 20 | 1,250 |
| Case registration and management REST API | 32 | 2,000 |
| Configurable approval workflow engine | 36 | 2,250 |
| Unique reference number generation | 12 | 750 |
| Document upload and storage management | 20 | 1,250 |
| Case search, filtering, and pagination | 16 | 1,000 |
| Audit trail and activity history | 20 | 1,250 |
| React frontend: case management views | 40 | 2,500 |
| React frontend: administration panel | 24 | 1,500 |
| PDF report generation | 16 | 1,000 |
| Docker deployment and environment setup | 16 | 1,000 |
| Testing (unit, integration, E2E) | 32 | 2,000 |
| QA, bug fixing, and technical documentation | 20 | 1,250 |

### Totals

- **Total hours:** 368
- **Total cost:** 23,000 EUR

### Recommended Team

- 1 Senior Backend Developer (technical lead)
- 1 Mid-level Full-Stack Developer
- 1 Frontend Developer
- 1 QA Engineer (part-time)

### Estimated Duration

**12 weeks** with a three-person development team and part-time QA support.""",
    },
    {
        "meeting_summary": (
            "An educational institution wants to build an online examination platform "
            "for professional certification programs. The system must allow administrators "
            "to create exams, manage question banks, configure time limits, and assign "
            "assessments to registered candidates. Candidates will complete exams through "
            "a responsive web interface with automatic answer saving and a countdown timer. "
            "The platform must integrate an existing identity verification service and "
            "record examination events such as tab switching, connection interruptions, "
            "and session expiration. Administrators need dashboards to monitor examination "
            "progress, review incidents, and export results to CSV and PDF. The institution "
            "already has a MySQL database and prefers a Laravel backend with a React "
            "frontend. The first release should support approximately 500 concurrent users."
        ),
        "estimation": """\
## Online Examination and Certification Platform

### Task Breakdown

| Task | Hours | Cost (EUR) |
|------|------:|------------|
| Requirements analysis and examination rules | 16 | 1,000 |
| Application architecture and database design | 20 | 1,250 |
| User authentication and role management | 16 | 1,000 |
| Question bank management module | 28 | 1,750 |
| Exam configuration and assignment module | 24 | 1,500 |
| Examination session and timer management | 28 | 1,750 |
| Automatic answer saving and recovery | 20 | 1,250 |
| Identity verification API integration | 20 | 1,250 |
| Examination event monitoring and logging | 24 | 1,500 |
| Automatic scoring and result calculation | 24 | 1,500 |
| React frontend: examination interface | 36 | 2,250 |
| React frontend: administration dashboard | 32 | 2,000 |
| CSV and PDF results export | 12 | 750 |
| Performance and concurrent user testing | 24 | 1,500 |
| Deployment and CI/CD configuration | 16 | 1,000 |
| Unit, integration, and E2E testing | 28 | 1,750 |
| QA, bug fixing, and documentation | 20 | 1,250 |

### Totals

- **Total hours:** 388
- **Total cost:** 24,250 EUR

### Recommended Team

- 1 Senior Full-Stack Developer (technical lead)
- 1 Backend Developer
- 1 Frontend Developer
- 1 QA Engineer (part-time)

### Estimated Duration

**14 weeks** with a three-person development team and part-time QA support.""",
    },
    {
        "meeting_summary": (
            "A regional logistics company needs a web platform to manage delivery orders "
            "and track shipments across multiple distribution centers. The system must "
            "allow operators to register orders, assign drivers and vehicles, update "
            "shipment statuses, and monitor deliveries through a centralized dashboard. "
            "Drivers will use a mobile-responsive web interface to confirm pickups and "
            "deliveries, upload proof-of-delivery photographs, and record delivery notes. "
            "The platform must integrate with an existing ERP through REST APIs and send "
            "automated email notifications when shipments are delayed or delivered. "
            "Managers need performance reports showing delivery times, pending orders, "
            "and driver productivity. The company prefers a Java Spring Boot backend, "
            "a React frontend, and PostgreSQL. The solution will be deployed to AWS "
            "and should initially support 50 drivers and 2,000 daily orders."
        ),
        "estimation": """\
## Logistics and Delivery Management Platform

### Task Breakdown

| Task | Hours | Cost (EUR) |
|------|------:|------------|
| Requirements analysis and logistics workflow design | 20 | 1,250 |
| System architecture and database modeling | 20 | 1,250 |
| Authentication and role-based access control | 16 | 1,000 |
| Delivery order management REST API | 28 | 1,750 |
| Driver and vehicle management module | 20 | 1,250 |
| Shipment assignment and status tracking | 32 | 2,000 |
| Proof-of-delivery photo upload and storage | 20 | 1,250 |
| ERP REST API integration | 28 | 1,750 |
| Automated email notification service | 16 | 1,000 |
| Delivery dashboard and operational metrics | 28 | 1,750 |
| React frontend: order and shipment management | 36 | 2,250 |
| Mobile-responsive driver interface | 32 | 2,000 |
| Reports and CSV export module | 16 | 1,000 |
| AWS infrastructure and deployment | 20 | 1,250 |
| Performance and load testing | 20 | 1,250 |
| Unit, integration, and E2E testing | 28 | 1,750 |
| QA, bug fixing, and documentation | 20 | 1,250 |

### Totals

- **Total hours:** 400
- **Total cost:** 25,000 EUR

### Recommended Team

- 1 Senior Backend Developer (technical lead)
- 1 Mid-level Backend Developer
- 1 Frontend Developer
- 1 QA Engineer (part-time)

### Estimated Duration

**14 weeks** with a three-person development team and part-time QA support.""",
    },
]


def format_examples_for_prompt(examples: list[dict]) -> str:
    """Format estimation examples into a string suitable for injection into a system prompt."""
    parts: list[str] = []
    for i, example in enumerate(examples, start=1):
        parts.append(
            f"--- EXAMPLE {i} ---\n"
            f"Meeting Summary:\n{example['meeting_summary']}\n\n"
            f"Estimation:\n{example['estimation']}\n"
        )
    return "\n".join(parts)
