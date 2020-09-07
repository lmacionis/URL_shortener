# url_shortener


About project:

This is django based url shortener, which creates new 6 digit/letter url, which you can edit through admin. 
It uses random algorithm. Though I was considering to use a 
base62 algorithm, but I run into a problem, which I didin't knew how to solve it 
and so I stayed with the random algorithm. In the future I might be changing it, 
depends on what I will learn about these two algorithms. Also, I will be updating
tests, because they are not covering all functionality, though it look like everything works
okey.


Installation:
1. Create new folder.
2. Create a virtual environment.
3. Create a file for repository.
4. Clone repository into the file.
5. Activate virtual environment.
6. Navigate to the file short_url.
7. Install file requirements.txt
8. Run commands makemigrations and migrate.
9. Create a superuser.
10. Run server on port 8000