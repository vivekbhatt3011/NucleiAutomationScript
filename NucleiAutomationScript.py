import subprocess
import argparse
import os

# Function to automate Nuclei scans
def run_nuclei(targets_file, templates, output_file):
    """
    Automates Nuclei scans for a list of targets.
    :param targets_file: Path to the file containing target URLs.
    :param templates: Path to Nuclei templates.
    :param output_file: Path to save scan results.
    """
    
    # Building the Nuclei command dynamically
    command = [
        "nuclei",
        "-l", targets_file,   # Load targets from a file
        "-t", templates,      # Use specified templates
        "-o", output_file,    # Save output results
        "-silent"             # Suppress unnecessary output
    ]
    
    try:
        # Running the Nuclei command and ensuring successful execution
        subprocess.run(command, check=True)
        print(f"Scan completed. Results saved to {output_file}")
    except subprocess.CalledProcessError as e:
        # Handling execution failures
        print(f"Error running Nuclei: {e}")

# Main execution block
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate Nuclei scanning")
    
    # Defining command-line arguments
    parser.add_argument("-l", "--list", required=True, help="File containing target URLs")
    parser.add_argument("-t", "--templates", required=True, help="Path to Nuclei templates")
    parser.add_argument("-o", "--output", default="nuclei_results.txt", help="Output file for results")
    
    # Parsing arguments
    args = parser.parse_args()
    
    # Calling the function with user-specified arguments
    run_nuclei(args.list, args.templates, args.output)
