
---

### **Migration Notes / Observability Docs**
`docs/migration_notes.md`:
```markdown
# Migration Notes

## Legacy to Prometheus
- Retired Nagios checks for CPU/memory
- Migrated app-specific metrics to custom exporters
- Set up alerting rules in Prometheus & routed to Slack via Alertmanager

## Observability Practices
- Metrics standardized via Prometheus format
- Dashboards monitor service-level and system-level metrics
- Alerts configured for critical thresholds and incident escalation
- Dockerized setup allows rapid replication and testing

