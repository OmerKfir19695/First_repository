"""
run_simulation.py

Script to run a single simulation based on user input or config.
"""

import argparse
from src.engine.kinetic_solver import run_kinetic_simulation

def main():
    parser = argparse.ArgumentParser(description="Run a kinetic simulation")
    parser.add_argument('--config', type=str, required=True, help="Path to config file (YAML or JSON)")
    args = parser.parse_args()

    # Placeholder: Load config and pass to simulation
    print(f"Running simulation with config: {args.config}")
    run_kinetic_simulation(args.config)

if __name__ == "__main__":
    main()
