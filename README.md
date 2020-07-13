# smartrutest
test run environment: platform win32 -- Python 3.7.4, pytest-5.4.3, py-1.9.0, pluggy-0.13.1

the test was run on the following browser Google Chrome 83.0.4103.116  (x64)

add chromedriver to the system path

if you want to run a test on the Linux environment, you will need to transfer the files forcibly encoded in utf-8, otherwise you will drop the tests at the stage of entering cyrillic characters

You need to download the project. then activate the test environment from the / env / folder. After that, run the file through a pytest

tests are not combined into one browser window and are not executed sequentially, because when a test crashes, all tests following it will also fail.

due to the large number of advertising not regulated by size, it is necessary to scroll through the elements using selenium. Therefore, jerking a page is acceptable in a visual test.

Added waiting time for weak test platforms and the Internet, so that the elements on the page can load.


demo video link: https://www.youtube.com/watch?v=DYo94lJPw1U

Thanks for your attention :)