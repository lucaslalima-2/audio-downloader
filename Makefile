# Variables
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Default target
all: check-ffmpeg venv install

# 1. Check if FFmpeg is installed on the system
check-ffmpeg:
	@command -v ffmpeg >/dev/null 2>&1 || { \
		echo "❌ Error: ffmpeg is not installed."; \
		echo "Install it with: 'brew install ffmpeg' (Mac) or 'sudo apt install ffmpeg' (Linux)"; \
		exit 1; \
	}
	@echo "✅ FFmpeg found."

# 2. Create virtual environment
venv:
	python3 -m venv $(VENV)
	@echo "✅ Virtual environment created."

# 3. Install dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencies installed."

# 4. Clean up
clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "🧹 Cleaned up project folder."

# 5. Run the script (Example: make run URL="https://...")
run:
	$(PYTHON) downloader.py "$(URL)"