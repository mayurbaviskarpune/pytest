# #!/bin/bash

# # Step 1: Create a virtual environment
# echo "Creating virtual environment..."
# python3 -m venv my_venv

# # Step 2: Activate the virtual environment
# echo "Activating virtual environment..."
# source my_venv/bin/activate

# # Step 3: Upgrade pip and install required packages
# echo "Installing pytest and allure plugins..."
# pip install --upgrade pip
# pip install pytest allure-pytest

# # Step 4: Verify installations
# echo "Verifying pytest installation..."
# pytest --version

# # Step 5: Deactivate virtual environment
# deactivate
# echo "Virtual environment setup completed! Use 'source my_venv/bin/activate' to activate."
#!/bin/bash

# Define Allure version
ALLURE_VERSION="2.24.0"
ALLURE_TGZ="allure-$ALLURE_VERSION.tgz"
ALLURE_URL="https://github.com/allure-framework/allure2/releases/download/$ALLURE_VERSION/$ALLURE_TGZ"
ALLURE_INSTALL_DIR="/opt/allure"
ALLURE_BIN="/usr/local/bin/allure"

# Step 1: Download Allure
echo "Downloading Allure $ALLURE_VERSION..."
curl -o $ALLURE_TGZ -L $ALLURE_URL

# Step 2: Extract Allure
echo "Extracting Allure..."
tar -zxvf $ALLURE_TGZ

# Step 3: Move Allure to /opt
echo "Moving Allure to $ALLURE_INSTALL_DIR..."
sudo mv "allure-$ALLURE_VERSION" $ALLURE_INSTALL_DIR

# Step 4: Create a symbolic link
echo "Creating symbolic link..."
sudo ln -sf $ALLURE_INSTALL_DIR/bin/allure $ALLURE_BIN

# Step 5: Verify Installation
echo "Verifying Allure installation..."
allure --version

echo "Allure installation completed successfully!"
