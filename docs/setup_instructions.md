# 1 - Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/username/enterprise-monitoring-migration.git
   cd enterprise-monitoring-migration

# 2 - Start the environment

    docker-compose up -d

# 3 - Access

    Prometheus: http://localhost:9090
    Grafana: http://localhost:3000 - (user: admin / pass: admin)
    Alertmanager: http://localhost:9093

# 4 - Import Grafana dashboards

    Go to Dashboards → Import and use JSON from grafana/dashboards

# 5 - Validate metrics:

    Prometheus → Targets → Verify custom_app_exporter and node_exporter
