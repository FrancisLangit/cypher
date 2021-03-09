![readme_banner](https://i.imgur.com/aZVdFXg.png)

Cypher is a open-source web application written on Python 3 using the Django web framework. One can make use of its features to translate English to various ciphers and vice-versa. It currently showcases algorithms that can translate to and from Binary, a Caesar Cipher, Morse Code, and Pig Latin.

For those interested, [a live version of the web application is available on Heroku.](https://cypher-web-app.herokuapp.com/)

![readme_gif_1](https://i.imgur.com/m3gef9V.gif)

## Installation

**Note:** This is for those that would like to be able to run the project locally and/or access its source code for contribution purposes. [A live version is available on Heroku](https://cypher-web-app.herokuapp.com/app/binary/) for convenient access.

1. Clone the repository or download it as a .zip file and extract it.

2. Navigate to the project's directory and enter `source cypher_venv/bin/activate` to activate its virtual environment. Once successfully done, one should see a `(cypher_venv)` as per below:

   ```bash
   cypher$ source cypher_venv/bin/activate
   (cypher_venv)cypher$
   ```

   If you're on Windows and using PowerShell use the command `cypher_venv/scripts/Activate` instead:

   ```powershell
   PS \cypher> cypher_venv/scripts/Activate
   (cypher_venv) PS \cypher>
   ```

3. Install the project's requirements on the virtual environment by entering `pip install -r requirements.txt`.

   ```bash
   (cypher_venv)cypher$ pip install -r requirements.txt
   ```

4. To run the website locally, enter `python manage.py runserver`.

   ```
   (cypher_venv)cypher$ python manage.py runserver
   Performing system checks...
   
   System check identified no issues (0 silenced).
   January 31, 2021 - 15:34:46
   Django version 3.1.5, using settings 'cypher.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

   Head on over to the link specified after `Starting development server at` on a web browser to use to the web application.

## Usage

![readme_gif_2](https://i.imgur.com/7t892B6.gif)

The above is a demo of the Caesar Cipher utility of the website. In this case, users will need to input a string of text, a ciphering key, and choose whether to make a submission for ciphering or deciphering. The application then outputs a string that the user can use. The Binary, Morse Code, and Pig Latin utilities of the website follow the same usage pattern, just without the need to provide a key. 

## Contributing

Pull requests are welcome for those that would like to make a  contribution.

For those that would like to apply major changes to the repository, we'd like to request that you open up an  issue first and discuss the changes you'd like to make.

## License

[MIT License](https://github.com/FrancisLangit/cypher/blob/master/LICENSE.txt)
