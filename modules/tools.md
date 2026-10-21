# Tool Policy

- Use local tools in `tools/` first for private or unpublished research material.
- Store secrets in environment variables or machine-local secret managers.
- Do not commit API keys, local tokens, private data dumps, or model binaries.

## Data Boundary

Local tools and local model endpoints may receive private project code, notes, logs,
retrieved context, and unpublished research material when needed for the task.

External tools may be used for public information lookup only. Before using web search,
network-capable MCP servers, package documentation services, issue trackers, or hosted
conversion tools, remove:

- private source code or data
- unpublished notes, papers, and research text
- credentials, tokens, keys, and local secrets
- private file paths, logs, stack traces, and environment details
- project-specific retrieved context

Use abstract descriptions for external lookup. For example, ask about a public package
API, error class, statistical method, or tool command without pasting project-specific
inputs or private output.

Ask the user before sending private context to an external tool, even when the tool is
read-only.
