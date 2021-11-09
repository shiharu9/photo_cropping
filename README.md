## photo_cropping

This project is aimed at educational institutions such as school, college, university, 
as well as various jobs that use online employee registration. This site helped to easily 
take a photo for registration and submission of documents online **when**:
- admission to an educational institution (online training);
- employment for remote work;
- creation and registration of online passes;
- and in other cases where an electronic photo of a person is needed.

### Selfie tips:
- a photo against a uniform background, for example a wall;
- the background should contrast with you. It should not merge with you;
- the lighting should be bright enough so that the photo is not darkened.

### Installation:
1. Clone a project from github:
```
git clone https://github.com/shiharu9/photo_cropping.git
```
2. Go to web folder:
```
cd photo_cropping/web
```
3. Create and run a virtual environment:
```
virtualenv env --no-site-packages

source env/bin/activate
```
4. Install project dependencies:
```
pip install -r ../requirements.txt
```
5. Start migrate:
```
python manage.py migrate
```
6. Start the server:
```
python manage.py runserver
```
