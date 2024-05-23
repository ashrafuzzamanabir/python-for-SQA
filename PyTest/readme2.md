## pytest report generation
   2 pytest --html=report.html <br>
   3 pytest --html=report.html <br>
   4 pip install pytest-cov <br>
   5 pytest --cov=stuff <br>
   6 pytest --cov=stuff --cov-report html <br>
   7 pytest --cov=stuff --cov-branch <br>
   8 pip install pytest-xdist <br>
   9 pytest -n 3
  ## API Testing  
  10 pip install requests <br>
  11 pytest tests/test_api.py <br>
  12 pytest ./tests/test_api.py <br>
  13 pytest tests/test_api.py <br>
  14 pytest tests/test_api.py <br>
  ## UI testing 
  15 pip install playwright
  16 pip install pytest-playwright<br>
  17 playwright install
  18 pytest tests/test_ui.py <br>
  19 pytest tests/test_ui.py <br>
  20 pytest tests/test_ui.py --headed --slowmo 1000 <br>