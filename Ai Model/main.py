import subprocess


def run_script(script_name):
    """Runs a Python script and captures its output."""
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"{script_name} output:\n{result.stdout}")

def main():
    # Train the model and save it
    print("Training the model...")
    run_script('train_model.py')
    
    # Use the trained model to make predictions
    print("Making predictions...")
    run_script('predict_and_save.py')

if __name__ == "__main__":
    main()
