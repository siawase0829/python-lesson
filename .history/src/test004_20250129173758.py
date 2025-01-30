from decorator_utils import my_decorator

@my_decorator
def main():
    # Create a new process by running the "process.py" Python script
    process = subprocess.Popen(["python", "process.py"])

    # Wait for the process to finish
    process.wait()

if __name__ == "__main__":
    main()
