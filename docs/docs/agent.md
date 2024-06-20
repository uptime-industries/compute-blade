---
sidebar_position: 8
displayed_sidebar: docsSidebar
---

# Compute Blade Agent
An OS agent interfacing with the Compute Blade hardware. 
### Functions
- Fan speed control
- LEDs
- Identify Blade
- Exposes hardware- and agent-related metrics using a Prometheus endpoint

## Install and Configuration
Detailed configuration options and install instructions are documented on GitHub

For most instaltion the following schript can be used
```bash
curl -L -o /tmp/compute-blade-agent-installer.sh https://raw.githubusercontent.com/uptime-industries/compute-blade-agent/main/hack/autoinstall.sh
chmod +x /tmp/compute-blade-agent-installer.sh
/tmp/compute-blade-agent-installer.sh
```