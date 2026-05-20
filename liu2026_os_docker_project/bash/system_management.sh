#!/bin/bash
# LIU-2026 - Bash System Management Automation
# This script collects system information and saves it in a report file.

REPORT_DIR="reports"
REPORT_FILE="$REPORT_DIR/system_report_$(date +%Y%m%d_%H%M%S).txt"

mkdir -p "$REPORT_DIR"

{
  echo "========================================"
  echo "        SYSTEM MANAGEMENT REPORT"
  echo "========================================"
  echo "Date: $(date)"
  echo "Hostname: $(hostname)"
  echo "Current user: $(whoami)"
  echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
  echo

  echo "========================================"
  echo "        OPERATING SYSTEM"
  echo "========================================"
  if [ -f /etc/os-release ]; then
    cat /etc/os-release
  else
    uname -a
  fi
  echo

  echo "========================================"
  echo "        CPU INFORMATION"
  echo "========================================"
  nproc 2>/dev/null && echo "CPU cores: $(nproc)"
  top -bn1 | head -5 2>/dev/null || echo "top command not available"
  echo

  echo "========================================"
  echo "        MEMORY INFORMATION"
  echo "========================================"
  free -h 2>/dev/null || echo "free command not available"
  echo

  echo "========================================"
  echo "        DISK USAGE"
  echo "========================================"
  df -h
  echo

  echo "========================================"
  echo "        RUNNING PROCESSES"
  echo "========================================"
  ps aux --sort=-%cpu | head -10 2>/dev/null || ps aux | head -10
  echo

  echo "========================================"
  echo "        NETWORK INFORMATION"
  echo "========================================"
  ip addr 2>/dev/null || ifconfig 2>/dev/null || echo "No network command available"

} > "$REPORT_FILE"

echo "Report generated successfully: $REPORT_FILE"
