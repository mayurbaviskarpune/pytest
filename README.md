#clone project 

git clone https://github.com/mayurbaviskarpune/pytest.git

#create environment run 

./pytest_setup.sh


#activate environment 

source  my_venv/bin/activate

#run test cases
pytest -v -s --alluredir=allure-results test_concept.py

#generate allure report 
allure serve /home/mayur/study/pytest/allure-results

Feature	                            Syntax
Install pytest	                    pip install pytest
Run all tests	                    pytest
Run specific test	                pytest test_file.py -k test_name
Parametrize tests	                @pytest.mark.parametrize("a, b, expected", [...])
Use fixtures	                    @pytest.fixture
Skip tests	                        @pytest.mark.skip(reason="reason")
