#!/bin/bash

echo "=================================================="
echo "Customer Support Ticket Analytics - Setup"
echo "=================================================="
echo ""

# Check Python version
echo "Checking Python version..."
python --version

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Setup complete!"
echo ""
echo "To run the project:"
echo "  1. python ticket_analytics.py       - Generate analytics dashboard"
echo "  2. python workflow_automation.py    - Run automation workflows"
echo "  3. python ticket_tagging.py     - Auto-tag tickets"
echo ""
echo "=================================================="
